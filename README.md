# PincodeSchoolSearch

This is a Django web application that lists the nearest schools in your area based on your provided pin code and coordinates.

<p align="center">
  <img src="/demo/PincodeSchoolSearch.gif" alt="GIF">
</p>

## Features

- Users can enter their pin code to see a list of schools in their area.
- Users can also enter their latitude and longitude coordinates for a more accurate location-based listing.
- The application calculates the shortest path between the user's location and each school, presenting the user with the nearest options.
- The schools listing is paginated to improve user experience, showing a default of 10 schools per page.
- User inputs (pin code and coordinates) are validated to ensure correctness and relevancy.

## Installation

Clone this repository into your local machine:

```
https://github.com/Ritesh11111111111111111111/PincodeSchoolSearch.git
```

Navigate into the project directory:

```
cd SchoolTripPlanner
```

Install the necessary packages:

```
pip install -r requirements.txt
```

## Usage

Ensure you are in the project directory and run the following commands:

```
python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```

Now open your web browser and navigate to `http://localhost:8000` to use the application.

## Forms

- **PincodeForm**: This form allows the user to input their pin code. It is validated to ensure it is a 6-digit number, adhering to the normal Indian pin code format.

- **CoordsForm**: This form accepts the user's latitude and longitude coordinates. It is not compulsory and if skipped, the location-based sorting is omitted.

## Models

- **School**: This is the model that represents a single School. It contains details like name, pin code, latitude, and longitude. Schools are filtered by pin code and sorted by distance using geopy.

## Dependencies

- Django: Python web framework used to build the application.
- geopy: Python library used to calculate distances based on latitude and longitude.
  
## Note
This application was developed with Django. It is also important to note that the calculating of distance based on user input coordinates is a fairly expensive operation in terms of computing power, particularly as the list of schools grows. In a production environment with thousands or more schools, you might consider offloading that computation to a background task or using a more efficient algorithm.

## Screenshots
<p align="center">
  <img src="/demo/1.png" alt="Image 1" width="100%">
</p>
<p align="center">
  <img src="/demo/2.png" alt="Image 3" width="47%">
  <img src="/demo/3.png" alt="Image 4" width="47%">
</p>
