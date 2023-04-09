from django.shortcuts import render
from django.http import HttpResponse
from app_money.models import *

from django.utils import timezone

# Create your views here.
def dashboard (request):
    
    money = MoneyFinance.objects.all()

    return render(request,'frontend/money.html',{'money':money})


def Add_money (request):
    return render (request,'backend/add_money.html')


def Edit_money (request):
    return render (request,'editfile/edit_money.html')

def Update_money (request):
    return render (request,'editfile/edit_money.html')

def Delete_money (request):
    return render (request,'deletefile/delete_money.html')


def Search_money (request):
    return render (request,'deletefile/delete_money.html')