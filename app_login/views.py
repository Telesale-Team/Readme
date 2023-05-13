
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
        "form":form
    }
    return render(request, 'html_login/register.html', context)

@user_passes_test(lambda u: u.is_superuser)  # Only superusers can access this view
@login_required
def delete_profile(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == 'POST':
        user.delete()
        return redirect('/user')  # Redirect to home page or any other appropriate page
    else:
        return render(request, 'html_login/delete_profile.html', {'user': user})