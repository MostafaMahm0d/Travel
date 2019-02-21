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

urlpatterns = [
     url(r'^$', views.index),
    url(r'^userlogin/$', auth_views.LoginView.as_view(template_name='login.html')),
    url(r'^userLogout/$', auth_views.LogoutView.as_view(template_name='index.html')),
    url(r'^register/$', views.register),
    url(r'^profile/$', views.profile),
    url(r'^profile/edit/$', views.profile_edit),

    
]
