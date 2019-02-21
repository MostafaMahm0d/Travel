from django import forms
from .models import Ride,customUser,Location


class RideForm (forms.ModelForm):
	class Meta :
		model = Ride
		fields = ('start_date','end_date','ride_from','ride_to',)


