from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from app_kpi.models import *
from app_team.models import *
from app_stock.models import *
from app_custom.models import *
from app_money.models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from .filters import *



# Create your views here.
@login_required(login_url="/")
def dashboard (request):

	filter_item = StockFilter(request.GET,queryset=Stock.objects.all())
	filter = filter_item.form
	item = filter_item.qs
	
	
	if request.method == "POST":
		form = StockForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/stock")
	else:
		form = StockForm()

	
	context = {

		"form"	:form,
		"filter":filter,
		"item":item,
  

	}
	return render(request,'html_stock/stock.html',context)

@login_required(login_url="/")
def Update_Stock (request,pk ):
	

	item = get_object_or_404(Stock, pk=pk)

	if request.method == "POST":
		form = StockForm(request.POST,request.FILES,instance=item)
		if form.is_valid():
			form.save()
			return redirect("/stock")
	else:
		form = StockForm(instance=item)
		
		
	context = {

		"item":item,
		"form": form,
	}

	return render (request,'html_stock/update_stock.html',context)

@login_required(login_url="/")
def Delete_Stock (request,pk ):
	

	item = get_object_or_404(Stock, pk=pk)


	if request.method == "POST":

		item.delete()
		return redirect("/stock")
	else:
		return render (request,'html_stock/delete_stock.html',{'item':item})

	

	

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

