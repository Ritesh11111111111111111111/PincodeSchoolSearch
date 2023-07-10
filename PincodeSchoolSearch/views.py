from django.shortcuts import render
from django.core.paginator import Paginator
from geopy.distance import geodesic

from .models import School
from .forms import PincodeForm, CoordsForm


def get_schools(page_number, pincode, user_coords):
    all_schools = School.objects.filter(pincode=pincode)
    if all(user_coords):
        user_coords_float = tuple(map(float, user_coords))
        all_schools = calculate_shortest_path(user_coords_float, list(all_schools))

    paginator = Paginator(all_schools, 10)
    return paginator.get_page(page_number)


def calculate_shortest_path(start_coords, school_list):
    remaining_schools = school_list[:]
    current_coords = start_coords
    route = []

    while remaining_schools:
        next_school = min(remaining_schools,
                          key=lambda school: geodesic(current_coords, (school.latitude, school.longitude)).miles)
        remaining_schools.remove(next_school)
        route.append(next_school)
        current_coords = (next_school.latitude, next_school.longitude)
    
    return route


def show_schools(request):
    form = PincodeForm(request.POST or None)
    form_coords = CoordsForm(request.POST or None)  # New form

    pincode = request.session.get('pincode')
    user_coords = request.session.get('user_coords')

    if form.is_valid():  # POST request
        pincode = form.cleaned_data.get('pincode')
        request.session['pincode'] = pincode  # Save the pincode in the session

        if form_coords.is_valid():
            latitude = form_coords.cleaned_data.get('latitude')
            longitude = form_coords.cleaned_data.get('longitude')

            if latitude and longitude:  # Make sure both fields have been filled in
                user_coords = (str(latitude), str(longitude))
                request.session['user_coords'] = user_coords

    page_number = request.GET.get('page')
    if 'page' in request.GET or form.is_valid():
        school_list = get_schools(page_number, pincode, user_coords)
    else:
        school_list = None

    return render(request, 'index.html', {'form': form, 'form_coords': form_coords, 'schools': school_list})