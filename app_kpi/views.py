from django.shortcuts import render,redirect
from django.http import HttpResponse
from app_kpi.models import *
from app_team.models import *
from app_stock.models import *
from django.utils import timezone


# Create your views here.

def Dashboard (request): 
    return render (request,'html_kpi/dashboard.html')  



def Add_dashboard (request):  

    return render (request,'html_kpi/add_dashboard.html')

