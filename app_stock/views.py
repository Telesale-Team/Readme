from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils import timezone
from app_kpi.models import *
from app_team.models import *
from app_stock.models import *
from app_custom.models import *
from app_money.models import *
from django.contrib.auth.decorators import login_required
from .forms import *



# Create your views here.
@login_required(login_url="/")
def dashboard (request):
	items = Stock.objects.all()
 
	if request.method == "POST":
		form = StockForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/stock")
	else:
		form = StockForm()

	context = {
		"items" : items,
		"form" : form,
	}
	return render(request,'html_stock/stock.html',context)

@login_required(login_url="/")
def Add_stock(request):
    
	items = Stock.objects.all()
	if request.method == "POST":
		form = StockForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/stock")
	else:
		form = StockForm()

	context = {
		"items" : items,
		"form" : form,
	}
	return render (request,'html_stock/add_Stock.html',context)
 


@login_required(login_url="/")
def Add_Category(request):

	items = Category.objects.all()
	if request.method == "POST":
		form = CategoryForm(request.POST )
		if form.is_valid():
			form.save()
			return redirect("/stock")
	else:
		form = CategoryForm()

	context = {
		"items" : items,
		"form" : form,
	}  
   
	return render (request,'html_stock/add_Category.html',context)




@login_required(login_url="/")
def Add_Item(request):
    
	items = Item.objects.all()
	if request.method == "POST":
		form = ItemFrom(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/stock")
	else:
		form = ItemFrom()

	context = {
		"items" : items,
		"form" : form,
	}    
	
	return render (request,'html_stock/add_Item.html',context)