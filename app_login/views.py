from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django import forms

# Create your views here.
def appregister (request):
    
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/user")
    else:
       form = CreateUser()
    
    
    return render(request,'html_login/register.html',{"form":form})