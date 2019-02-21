"""first_project URL Configuration

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
from django.conf.urls import url
from lonely_planet import views
from experience.views import *

urlpatterns = [
    # url(r'^$', views.index, name="index"),
    url(r'^countries/$',views.countries ,name="countries"),    
    url(r'^country/(?P<country_id>[0-9]+)$' , views.singlcountry , name="singlcountry"),
    url(r'^city/(?P<city_id>[0-9]+)$' , views.singlcity , name="singlcity"),
    url(r'^location/(?P<location_id>[0-9]+)$' , views.singllocation , name="singllocation")


    # url(r'^new$', views.new, name='new'),
    # url(r'^student/edit(?P<student_id>[0-9]+)$',views.edit, name='edit')
]
