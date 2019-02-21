from django.contrib import admin
from car_rental.models import Location,Ride
from reservation.models import Reservation,Hotel
from .models import customUser

admin.site.register(Ride)
admin.site.register(customUser)
admin.site.register(Location)
admin.site.register(Hotel)
admin.site.register(Reservation)


# Register your models here.
