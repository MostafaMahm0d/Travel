from django.conf.urls import url,include
from reservation import views

urlpatterns = [
    url(r'^add$', views.add_reservation),
]
