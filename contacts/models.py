from django.db import models

# Create your models here.

class contactRecords(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=15)  # varchar datatype
    email = models.CharField(max_length=25)
    dob = models.DateField()
    address = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)


