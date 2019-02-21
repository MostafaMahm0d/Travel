from django.db import models
from blogapp.models import *
from lonely_planet.models import *
# from car_rental.models import *
# from reservation.models import *


# Create your models here.
class Experience(models.Model):
	user=models.ForeignKey(customUser, null = True)
	city=models.ForeignKey(City)
	message=models.CharField(max_length=300)
	rate=models.IntegerField(default=1)

	def __str__(self):
		return self.message

class Comments(models.Model):
	comment=models.CharField(max_length=200)
	experience=models.ForeignKey(Experience, null = True)
	user=models.ForeignKey(customUser, null = True)
	def __str__(self):
		return self.comment