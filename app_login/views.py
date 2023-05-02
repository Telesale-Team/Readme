from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import *

# Create your views here.
def appregister (request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if forms.is_valid():
            form.save()
            return redirect("/register")
    else:
       form = UserCreationForm()
    
    
    return render(request,'html_login/register.html',{"form":form})