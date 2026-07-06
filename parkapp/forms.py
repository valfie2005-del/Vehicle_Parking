from django import forms
from .models import Parking

class ParkingForm(forms.ModelForm):
    class Meta:
        model = Parking
        fields = '__all__'

        labels = {
            'Pid': 'Product ID',
            'Vehicle_Type' : 'Vehicle Type',
            'Vehicle_number' : 'Vehicle Number' ,
            'owner_name' : 'Owner Name' ,
            'parked_hours' : 'Parked hours',
            'paid_amount' : 'Paid_Amount' ,
            'status': 'Status',

        }

        widgets  ={
            'Pid' : forms.NumberInput(attrs={'placeholder': 'eg. 101'}),
            'Vehicle_Type' : forms.TextInput(attrs={'placeholder': 'eg. Car/Bike'}),
            'Vehicle_number' : forms.TextInput(attrs={'placeholder': 'eg. TN 75 AK ****'}),
            'owner_name' : forms.TextInput(attrs={'placeholder': 'eg. John Henry'}),
            'parked_hours' : forms.TextInput(attrs={'placeholder': 'eg. 2 hr'}),
            'paid_amount' : forms.NumberInput(attrs={'placeholder': 'eg. $200'}),
            'status': forms.TextInput(attrs={'placeholder': 'eg. Active'}),
        }