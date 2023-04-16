from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateNewRegisterForm

# Create your views here.
def appregister (request):
    
	if request.method == "POST":	
		form = CreateNewRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/login")
   
	 
	else:
		form = CreateNewRegisterForm()
		
	
	
	context = {
		
		"form":form
	}
	
	return render(request,'html_login/register.html',context)