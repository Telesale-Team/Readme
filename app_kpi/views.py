from django.shortcuts import render,redirect
from django.http import HttpResponse
from app_kpi.models import *
from app_team.models import *
from app_stock.models import *
from django.utils import timezone


# Create your views here.
def index(request):

    scores = Kpi.objects.all()
    
    current_datetime = timezone.now()    
    date = current_datetime.strftime('%d-%m-%Y')
    time = current_datetime.strftime('%H:%M:%S')
    
   

    return redirect('/login')


def Dashboard (request):  

    return render (request,'frontend/dashboard.html')


def Add_dashboard (request):  

    return render (request,'backend/add_dashboard.html')


def Add_money (request):
    
    return render (request,'backend/add_money.html')
