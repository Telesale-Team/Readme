from django.shortcuts import render,redirect
from django.http import HttpResponse
from app_user.models import *
from app_login.forms import *
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def Dashboard (request):

    users = User.objects.all().order_by('-username')
    quatity = list(users)
    
    CreateUser
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            redirect("user/")
    else:
        form = CreateUser()
        redirect("user/")
        
            
    context = {
        "quatity":len(quatity),
        "users":users,
        "form": form


    }
    
    return render (request,'html_user/dashboard_user.html',context)


def Add_user (request):
    
    return render(request,'html_user/add_user.html')


def Profile (request,email ):
    

    user = User.objects.filter( email = email )
    
    return render(request,'html_user/profile_user.html',{'user':user})


def Delete_user (request):
    return render(request,'html_user/delete_user.html')


def Update_user(request):
    return render(request,'html_user/update_user.html')


def Edit_user (request):
    
    
    return render(request,'html_user/edit_user.html')


def Report_user (request):
    return render(request,'html_user/report_user.html')