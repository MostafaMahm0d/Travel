from django.db import models
from blogapp.models import *
# from experience.models import *
from lonely_planet.models import *
from datetime import datetime    

# from car_rental.models import *

# Create your models here.
# class Hotel(models.Model):
# 	hotel_name =models.CharField(max_length = 50)
# 	def __str__(self):
# 		return self.hotel_name

class Reservation(models.Model):
	user = models.ForeignKey(customUser)
	hotel = models.ForeignKey(Hotel)
	reservatin_date = models.DateTimeField(default=datetime.now(), blank=True)
	start_date = models.DateField()
	end_date = models.DateField()
	guest= models.IntegerField()
	