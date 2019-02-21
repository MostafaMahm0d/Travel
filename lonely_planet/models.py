from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# from experience.models import *
# from blogapp.models import *
# from car_rental.models import *
# from reservation.models import *
# Create your models here.



class Country(models.Model):
    country_name = models.CharField(max_length = 200)
    country_description = models.CharField(max_length = 250, default="")
    country_rate = models.IntegerField(default='0',validators=[MinValueValidator(0),
                                       MaxValueValidator(195)])
    country_image = models.ImageField(upload_to = 'static/' ,blank = True )

    def __str__(self):
        return self.country_name

class City(models.Model):
    city_name = models.CharField(max_length = 200)
    city_rate = models.IntegerField(default='0',validators=[MinValueValidator(0),
                                       MaxValueValidator(195)])
    city_description = models.CharField(max_length = 250 , default="")
    city_image = models.ImageField(upload_to = 'static/' ,blank = True )
    country = models.ForeignKey(Country)

    def __str__(self):
        return self.city_name
    

class Location(models.Model):
    location_name = models.CharField(max_length = 200)
    location_description = models.TextField(default="")
    location_image = models.ImageField(upload_to = 'static/' ,blank = True)
    city = models.ForeignKey(City)

    def __str__(self):
        return self.location_name

class Hotel(models.Model):
    hotel_name = models.CharField(max_length = 250)
    hotel_image = models.ImageField(upload_to = 'static/' ,blank = True )
    city = models.ForeignKey(City)
    
    def __str__(self):
        return self.hotel_name



     


