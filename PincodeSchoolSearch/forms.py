from django import forms

class PincodeForm(forms.Form):
    pincode = forms.IntegerField(
        required=True,
        error_messages={'required': 'Please enter a pin code'},
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter Pin Code'})
    )

    def clean_pincode(self):
        pincode = self.cleaned_data.get('pincode')
        if len(str(pincode)) != 6:  # Assuming it is an Indian Pin Code with 6 digits 
            raise forms.ValidationError('Enter a valid 6 digits pin code')
        return pincode
    
class CoordsForm(forms.Form):
    latitude = forms.DecimalField(max_digits=9, decimal_places=6, label='Your latitude', required=False)
    longitude = forms.DecimalField(max_digits=9, decimal_places=6, label='Your longitude', required=False)