"""Travelling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from blogapp import views 
from lonely_planet import views as lonely
from reservation import views as reservation
from car_rental import views as car_rental 

urlpatterns = [
     url(r'^$', views.index),
    url(r'^userlogin/$', auth_views.LoginView.as_view(template_name='login.html')),
    url(r'^userLogout/$', auth_views.LogoutView.as_view(template_name='index.html')),
    url(r'^register/$', views.register),
    url(r'^profile/$', views.profile),
    url(r'^profile/edit/$', views.profile_edit),
    url(r'^countries/$',lonely.countries ,name="countries"),    
    url(r'^country/(?P<country_id>[0-9]+)$' , lonely.singlcountry , name="singlcountry"),
    url(r'^city/(?P<city_id>[0-9]+)$' , lonely.singlcity , name="singlcity"),
    url(r'^city/reserveHotel/(?P<city_id>[0-9]+)$' , reservation.add_reservation , name="reservehotel"),
    url(r'^city/CarRent/(?P<city_id>[0-9]+)$' , car_rental.add_car_rental, name="CarRent"),
    url(r'^location/(?P<location_id>[0-9]+)$' , views.singllocation , name="singllocation")

    
]
