from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from app_kpi.models import *
from app_team.models import *
from app_stock.models import *
from app_custom.models import *
from app_money.models import *


# Create your views here.
def dashboard (request):
    items = Stock.objects.all()
    return render(request,'html_stock/stock.html',{"items":items})

    
def Add_stock(request):     
     return render (request,'html_stock/add_Stock.html')