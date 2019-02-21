from .models import Experience,Comments
from django import forms
class Expform (forms.ModelForm):
	class Meta:
		model=Experience
		fields=('message','rate',)

class Commentform (forms.ModelForm):
	class Meta:
		model=Comments
		fields=('comment',)