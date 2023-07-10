from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)  # the school's name
    address = models.CharField(max_length=300)  # the school's address
    pincode = models.CharField(max_length=20)  # the pincode of the school
    latitude = models.FloatField()  # to help pinpoint the location for route optimization
    longitude = models.FloatField()  # to help pinpoint the location for route optimization

    def __str__(self):
        return self.name