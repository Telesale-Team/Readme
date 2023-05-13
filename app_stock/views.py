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
	notebook = Notebook.objects.all()
	cable = Cable.objects.all()
	office = Office.objects.all()
	category = Category.objects.all()
	Q_notebook = notebook.count()
	
	print('Text',Q_notebook)

	context = {
		"notebook" : notebook,
		"cable" : cable,
  		"office" : office,
		"category" : category,
		"Q_notebook":Q_notebook,
  

	}
	return render(request,'html_stock/stock.html',context)



@login_required(login_url="/")
def Add_stock(request):
    
	items = Stock.objects.all()
	qutity_item = len(items)
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
		"qutity_item":qutity_item,
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

@login_required(login_url="/")
def Add_Cable (request):
    
	cable = Cable.objects.all()
	if request.method == "POST":
		form = CableForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("add-cable")
	else:
		form = CableForm()

	context = {
		"cable" : cable,
		"form" : form,
	}    
	
	return render (request,'html_stock/add_cable.html',context)

@login_required(login_url="/")
def Add_Notebook (request):
    
	items = Notebook.objects.all()
	if request.method == "POST":
		form = NotebookForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/stock")
	else:
		form = NotebookForm()

	context = {
		"items" : items,
		"form" : form,
	}    
	
	return render (request,'html_stock/add_notebook.html',context)

@login_required(login_url="/")
def Add_Office (request):
    
	office = Office.objects.all()
	if request.method == "POST":
		form = OfficeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/stock")
	else:
		form = OfficeForm()

	context = {
		"office" : office,
		"form" : form,
	}    
	
	return render (request,'html_stock/add_office.html',context)

@login_required(login_url="/")
def Pickup (request,id):

    items = Notebook.objects.get(id=id)
    
    if request.method == "POST":
        form = NotebookForm(request.POST,instance=items)
        if form.is_valid():
            form.save()
            return redirect("add_notebook")
    else:
        form = NotebookForm(instance=items)
        
        
    context = {
        "items":items,
		"form": form,
	}
    
    return render (request,'html_stock/pickup_notebook.html',context)