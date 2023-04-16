from django.shortcuts import render
from django.http import HttpResponse
from app_kpi.models import *
from app_team.models import *
from app_stock.models import *
from django.utils import timezone


# Create your views here.
def index (request):
    return render(request,'html_customer/customer.html')


def Add_custom (request):
    return render (request,'html_customer/add_customer.html')


def Edit_custom (request):
    return render (request,'html_customer/edit_customer.html')

def Update_custom (request):
    return render (request,'html_customer/edit_customer.html')

def Delete_custom (request):
    return render (request,'html_customer/delete_customer.html')


def Search_custom (request):
    return render (request,'html_customer/delete_customer.html')

def Report_custom (request):
    return render (request,'html_customer/report_customer.html')