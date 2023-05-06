from django.shortcuts import render
from django.http import HttpResponse
from app_money.models import *
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.
@login_required(login_url="/")
def dashboard (request):
    
    view_money = ReceiptInvoice.objects.all()
    


    return render(request,'html_money/money.html',{"view_money":view_money})

@login_required(login_url="/")
def Add_money (request):
    return render (request,'html_money/add_money.html')

@login_required(login_url="/")
def Edit_money (request):
    return render (request,'html_money/edit_money.html')
@login_required(login_url="/")
def Update_money (request):
    return render (request,'html_money/edit_money.html')
@login_required(login_url="/")
def Delete_money (request):
    return render (request,'html_money/delete_money.html')

@login_required(login_url="/")
def Search_money (request):
    return render (request,'html_money/search_money.html')