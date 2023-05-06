from django.shortcuts import render,redirect
from django.http import HttpResponse
from app_kpi.models import *
from app_team.models import *
from app_stock.models import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
@login_required(login_url="/")
def Dashboards (request):
    thaiban = Customer_Interest.objects.all()[:5]
    
    number = len(thaiban)
    
    context = {
		"thaiban" : thaiban,
		"number" : number,
	}
    
    return render (request,'html_kpi/dashboard.html',context)  


@login_required(login_url="/")
def Add_dashboard (request):
	
	if request.method == "POST":
		form = KipForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/user")
	else:
		form = KipForm()

		
			
	context = {

		"form": form


	}
	 
	return render (request,'html_kpi/add_dashboard.html',context)   

 
@login_required(login_url="/")

def Thaibans (request):
    thaiban = Customer_Interest.objects.all()
    if request.method == "POST":
        form = ThaibanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/dashboard/thaiban")
    else:
        form = ThaibanForm()

        
            
    context = {

        "form": form,
		"thaiban":thaiban,

    }
     
    return render (request,'html_kpi/thaiban.html',context)   