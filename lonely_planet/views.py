from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from experience.models import * 
from experience.views import * 
# Create your views here.


def index(request):
    country_fromDB = Country.objects.all()
    context = {'country': country_fromDB}
    return render(request,'index.html' ,context)
############################################
def countries(request):
    country_fromDB = Country.objects.all()
    context = {'country': country_fromDB}
    return render(request,'countries_list.html' ,context)
# #############################################
def singlcountry(request,country_id):
    countrylist_fromDB = Country.objects.all()
    country_fromDB = Country.objects.get(id = int(country_id))
    cities_fromDB = City.objects.filter(country_id = int(country_id))
    context = {'country':country_fromDB,'countrylist':countrylist_fromDB ,"City":cities_fromDB}
    return render(request, 'country.html',context)
###############################################
# def singlcity(request,city_id):
#     city_fromDB = City.objects.get(id = int(city_id))
#     locations_fromDB = Location.objects.filter(city_id =int(city_id) )
#     hotels_fromDB = Hotel.objects.filter(city_id =int(city_id) )
#     experience_fromDB =Experience.objects.filter(city=int(city_id))
#     user=customUser.objects.all()
#     context = { "city":city_fromDB, "location":locations_fromDB,"allexp": experience_fromDB, "hotel":hotels_fromDB,"user":user}
#     return render(request, 'city.html',context)
def singlcity(request,city_id):
    city_fromDB = City.objects.get(id = int(city_id))
    locations_fromDB = Location.objects.filter(city_id =int(city_id) )
    hotels_fromDB = Hotel.objects.filter(city_id =int(city_id) )
    # experience_fromDB =Experience.objects.select_related()
    experience_fromDB =Experience.objects.filter(city=int(city_id))
    user=customUser.objects.all()
    context = { "city":city_fromDB, "location":locations_fromDB,"allexp": experience_fromDB, "hotel":hotels_fromDB,"user":user}
    return render(request, 'city.html',context)
################################################    
def singllocation(request,location_id):
    location_fromDB = Location.objects.get(id = int(location_id))
    context = { "location":location_fromDB}
    return render(request, 'location.html',context)
# #############################################
# def edit(request,student_id):
#     student_fromDB = Student.objects.get(id = int(student_id))
#     if request.method == 'POST':  #randring form with data of student
#         form = StudentForm(request.POST, instance = student_fromDB )
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/app1')
#     else:
#         form = StudentForm( instance = student_fromDB )
#         context = {'st_form': form }
#         return render(request , 'form.html' , context)