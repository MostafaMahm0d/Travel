from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from lonely_planet.models import *
from lonely_planet.views import *

# Create your views here.
def Country_rat():
    return Country.objects.all().order_by('-country_rate')[:6]
def City_rat():
    return City.objects.all().order_by('-city_rate')[:6]    
    
def index(request):
    country_fromDB = Country.objects.all()
    context = {'country': country_fromDB,"Top_countries":Country_rat(),"top_city":City_rat(),"range":range(0,5)}

    return render(request,'index.html' ,context)

def userlogin(request):
     return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST,request.FILES)
        
        if form.is_valid():
          
            form.save()
            username = form.cleaned_data.get('username')
            password= form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('/Travelling')
            else:
                return render(request, 'register.html', {'form': form})     
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})     

@login_required
def profile_edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user)

        if u_form.is_valid() and p_form.is_valid():
            print("vvv")
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('/Travelling/profile/')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user)
        #print(u_form.username)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    print("nnnnn")
    return render(request, 'edit.html', context)
@login_required
def profile(request):
     return render(request, 'profile.html')    