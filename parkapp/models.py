from django.db import models

from django.db import models

# Create your models here.
class Parking(models.Model):
    Pid = models.IntegerField(primary_key=True)
    Vehicle_type = models.CharField(max_length=20)
    Vehicle_number = models.CharField(max_length=20)
    owner_name = models.CharField(max_length=20)
    parked_hours = models.TextField(max_length=20)
    paid_amount = models.IntegerField()
    status = models.CharField(max_length=50)

