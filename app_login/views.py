
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app_user.models import ProfileUser
from .forms import *
from django import forms

# Create your views here.

def register(request):
    users = ProfileUser.objects.all()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.save()
            ProfileUser.objects.create(username=username)
            
            return redirect('/user')  # Redirect to user profile page
    else:
        form = RegistrationForm()
        
        
    context = {
        "users":users,
        "form":form,
    }
    return render(request, 'html_login/register.html', context)
