from django.shortcuts import render
from django.http import HttpResponse
from app_kpi.models import *
from app_team.models import *
from app_stock.models import *
from django.utils import timezone


# Create your views here.
def index (request):
    return render(request,'frontend/customer.html')


def Add_custom (request):
    return render (request,'backend/add_customer.html')


def Edit_custom (request):
    return render (request,'editfile/edit_customer.html')

def Update_custom (request):
    return render (request,'editfile/edit_customer.html')

def Delete_custom (request):
    return render (request,'deletefile/delete_customer.html')


def Search_custom (request):
    return render (request,'deletefile/delete_customer.html')

def Report_custom (request):
    return render (request,'deletefile/report_customer.html')