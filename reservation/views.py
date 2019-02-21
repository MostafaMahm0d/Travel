from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReservationForm
from lonely_planet.models import * 

# Create your views here.
# def add_reservation(request):
# 	form =  ReservationForm()
# 	if(request.method == 'POST'):
# 		form = ReservationForm(request.POST)
# 		if(form.is_valid()):
# 			form.save()
# 			return  HttpResponseRedirect('/')


# 	return render(request,'add_reservation.html',{'form':form})


def add_reservation(request,city_id):
	hotels_fromDB = Hotel.objects.filter(city_id =int(city_id) )
	form =  ReservationForm()
	if(request.method == 'POST'):
		form = ReservationForm(request.POST)
		if(form.is_valid()):
			post = form.save(commit = False)
			post.user = request.user
			post.save()
			return  HttpResponseRedirect('/Travelling')


	return render(request,'add_reservation.html',{'form':form,'hotels':hotels_fromDB})

