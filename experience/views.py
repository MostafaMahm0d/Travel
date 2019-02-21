from django.shortcuts import render
from .models import Experience,Comments
from django.http import HttpResponse
from .forms import Expform ,Commentform 
from django.http import HttpResponseRedirect
from lonely_planet.models import City
# from blogapp.views import *
from blogapp.models import *



def getallexp(request, city_id):
	all_exp=Experience.objects.filter(city_id = int(city_id))
	context={'allexp':all_exp}
	return all_exp

def getexp(request,exp_id):
	exp=Experience.objects.filter(city_id_id=exp_id)
	# comment=Comments.objects.get(experience_id=exp_id)
	# context={'exp':exp,'comment':comment}
	print(exp)
	context={'exp':exp}
	return 	exp

def getexp(request,exp_id):
	exp=Experience.objects.get(id=exp_id)
	# comment=Comments.objects.get(experience_id=exp_id)
	# context={'exp':exp,'comment':comment}
	print(exp)
	context={'exp':exp}
	return 	exp

def getcomment(request,exp_id):
	exp=Experience.objects.get(id=exp_id)
	comment=Comments.objects.filter(experience_id=exp_id)
	if comment:
		comment=Comments.objects.get(experience_id=exp_id)

		context={'comment':comment,'exp':exp}	
		return render (request,'comment.html',context)
	else:
		context={'exp':exp}
		return render (request,'comment.html',context)
def new (request,city_id):
	if request.method=='POST' :
		form=Expform(request.POST)
		if form .is_valid() :
			p1=form.save(commit=False)
			ex=City.objects.get(id=eval(city_id))
			p1.city =ex
			p1.user=request.user
			p1.save()
			form.save()
			return HttpResponseRedirect('')
		return render (request,'new.html',context)
	else:
		form=Expform()
		context={'exp_form':form}
		return render (request,'new.html',context)


def newcomment (request,exp_id):
	exp=Experience.objects.get(id=exp_id)
	comment=Comments.objects.filter(experience_id=exp_id)
	# print(comment)
	user=customUser.objects.all()
   
	# context={'comment':comment,'exp':exp}
	# return render (request,'comment.html',context)

	form=Commentform()
	if request.method=='POST' :
		form= Commentform(request.POST)
		# form.experience_id =request.Experience

		if form .is_valid() :
			p1=form.save(commit=False)
			ex=Experience.objects.get(id=eval(exp_id))
			p1.experience=ex
			p1.user=request.user

			p1.save()
			return HttpResponseRedirect('')
		return render (request,'creatcomm.html',{"form":form})
	else:
		form= Commentform()
		context={'comment_form':form,'comment':comment,'exp':exp,'user':user}
		return render (request,'creatcomm.html',context)

def update(request,exp_id):	
	ex=Experience.objects.get(id=eval(exp_id))
	if request.method=='POST' :
		form=Expform(request.POST,instance=ex)
		if form .is_valid() :
			form.save()
			return HttpResponseRedirect('/experience/home')
		return render (request,'new.html',context)
	else:
		form=Expform(instance=ex)
		context={'exp_form':form}
		return render (request,'new.html',context)

def delete(request,exp_id):
	st=Experience.objects.get(id=eval(exp_id))
	st.delete()
	return HttpResponseRedirect('/experience/home')
