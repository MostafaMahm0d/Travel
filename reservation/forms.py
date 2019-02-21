from django import forms
from .models import Reservation ,customUser,Hotel

class ReservationForm (forms.ModelForm):
	class Meta :
		model = Reservation
		fields = ('hotel','start_date','end_date','guest')
