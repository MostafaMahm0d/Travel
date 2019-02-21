"""project URL Configuration

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
from experience import views 	
urlpatterns = [
    # url(r'^(?P<user_name>[a-zA-Z]+)$',views.hellouser)
    url(r'^home$',views.getallexp),
    url(r'^exp/(?P<exp_id>[0-9]+)$',views.getexp),
    url(r'^update/(?P<exp_id>[0-9]+)$',views.update),
    url(r'^delete/(?P<exp_id>[0-9]+)$',views.delete),
    url(r'^comm/(?P<exp_id>[0-9]+)$',views.getcomment),
    url(r'^(?P<city_id>[0-9]+)/new$', views.new),
    # url(r'^city/(?P<city_id>[0-9]+)/comm/(?P<exp_id>[0-9]+)$', views.newcomment ),
    url(r'^experience/(?P<exp_id>[0-9]+)$', views.newcomment ),

    ]