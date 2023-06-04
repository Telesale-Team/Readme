from django.shortcuts import render,redirect
from django.http import HttpResponse
from app_kpi.models import *
from app_team.models import *
from app_stock.models import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import *
from app_sale.models import *

# Create your views here.
@login_required(login_url="/")
def Dashboards (request):
 
    context = {
        # source = Live(3) SEO(2) ADS(1)
        # Web = Mughuay(4) Duckbet(3) Thaibaan(2) 7RX7(1)
        
        #SEO 7RX7
        "seo_rx" : Sale.objects.all().filter(source=2,web=1).count(), 
        "seo_rx_buy" : Sale.objects.all().filter(source=2,web=1,buy="ซื้อ").count(),
        "seo_rx_nobuy" : Sale.objects.all().filter(source=2,web=1,buy="ยังไม่ซื้อ").count(),
        
        # SEO Duckbet
        "seo_duckbet" : Sale.objects.all().filter(source=2,web=3).count(),
        "seo_duckbet_buy" : Sale.objects.all().filter(source=2,web=3,buy="ซื้อ").count(),
        "seo_duckbet_nobuy" : Sale.objects.all().filter(source=2,web=3,buy="ยังไม่ซื้อ").count(),
        
        # SEO Thaibaan
        "seo_thaibaan_all" : Sale.objects.all().filter(source=2,web=2).count(),
        "seo_thaibaan_buy" : Sale.objects.all().filter(source=2,web=2,buy="ซื้อ").count(),
        "seo_thaibaan_nobuy" : Sale.objects.all().filter(source=2,web=2,buy="ยังไม่ซื้อ").count(),
        
        # Live 7RX7
        "seo_thaibaan_all" : Sale.objects.all().filter(source=3,web=2).count(),
        "seo_thaibaan_buy" : Sale.objects.all().filter(source=3,web=2,buy="ซื้อ").count(),
        "seo_thaibaan_nobuy" : Sale.objects.all().filter(source=3,web=2,buy="ยังไม่ซื้อ").count(),

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

		"form": form,
        

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