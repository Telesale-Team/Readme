from django.shortcuts import render
from django.http import HttpResponse
from app_user.models import *

# Create your views here.
def Dashboard (request):

    users = ProfileUser.objects.all()

    return render (request,'html_user/dashboard_user.html',{'users':users})


def Add_user (request):
    
    return render(request,'html_user/add_user.html')


def Profile (request,id_user ):
    

    user = ProfileUser.objects.filter(id_user = id_user)
    
    return render(request,'html_user/profile_user.html',{'user':user})


def Delete_user (request):
    return render(request,'html_user/delete_user.html')


def Update_user(request):
    return render(request,'html_user/update_user.html')


def Edit_user (request):
    
    
    return render(request,'html_user/edit_user.html')


def Report_user (request):
    return render(request,'html_user/report_user.html')