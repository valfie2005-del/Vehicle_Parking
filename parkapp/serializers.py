from rest_framework import serializers
from .models import Parking

class ParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = ['Pid', 'Vehicle_type', 'Vehicle_number', 'owner_name', 'parked_hours', 'paid_amount' , 'status']