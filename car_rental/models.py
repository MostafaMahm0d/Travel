from django.db import models
# from experience.models import *
from blogapp.models import *
from lonely_planet.models import *
from datetime import datetime    

# from reservation.models import *
# from django.contrib.auth.models import customUser
# Create your models here.

# class Location(models.Model):
# 	loction_name = models.CharField(max_length = 50)
# 	def __str__(self):
# 		return self.loction_name

	




class Ride (models.Model):
	user= models.ForeignKey(customUser)
	Ride_date = models.DateTimeField(default=datetime.now(), blank=True)
	start_date = models.DateField()
	end_date  = models.DateField()
	ride_from = models.ForeignKey(Location,related_name ='from_location')
	ride_to  = models.ForeignKey(Location,related_name = 'to_location')







