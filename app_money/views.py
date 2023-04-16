from django.shortcuts import render
from django.http import HttpResponse
from app_money.models import *

from django.utils import timezone

# Create your views here.
def dashboard (request):
    
    view_money = ReceiptInvoice.objects.all()
    


    return render(request,'html_money/money.html',{"view_money":view_money})


def Add_money (request):
    return render (request,'html_money/add_money.html')


def Edit_money (request):
    return render (request,'html_money/edit_money.html')

def Update_money (request):
    return render (request,'html_money/edit_money.html')

def Delete_money (request):
    return render (request,'html_money/delete_money.html')


def Search_money (request):
    return render (request,'html_money/search_money.html')