from django.shortcuts import render
from .forms import RideForm 
from django.http import HttpResponseRedirect
from lonely_planet.models import Location

# Create your views here.

# def index(request):
# 	print(Student.objects.all())
# 	context = {'student_list':Student.objects.all()}
# 	return render(request,'index.html',context)

# def add_car_rental(request):
# 	form =  RideForm()
# 	if(request.method == 'POST'):
# 		form = RideForm(request.POST)
# 		if(form.is_valid()):
# 			form.save()
# 			return  HttpResponseRedirect('/')


# 	return render(request,'add_car_rental.html',{'form':form})


def add_car_rental(request,city_id):
	form =  RideForm()
	location_per_city = Location.objects.filter(city =int(city_id))
	if(request.method == 'POST'):
		form = RideForm(request.POST)
		if(form.is_valid()):
			post = form.save(commit = False)
			post.user = request.user
			post.save()
			return  HttpResponseRedirect('/Travelling')


	return render(request,'add_car_rental.html',{'form':form,'locations':location_per_city})