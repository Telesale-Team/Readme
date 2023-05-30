from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from app_sale.forms import *
from app_sale.filters import *
from app_sale.models import *
from django.core.paginator import Paginator


# Create your views here.

@login_required(login_url="/")
def Index (request):
	sale = Sale.objects.all()
	
	#Form
	if request.method == "POST":
		form_sale = SaleForm(request.POST)
		if form_sale.is_valid():
			form_sale.save()
			return redirect("sale-home")
	else:
		form_sale = SaleForm()	
	
	#Filter
	filter = SaleFilter(request.GET,queryset=Sale.objects.all())
	filter_stock = filter.form
	query_stock = filter.qs
	
 
	#Paginator
	page = Paginator(sale,10)
	page_list = request.GET.get("page")
	page_sale = page.get_page(page_list)
	context = {

		"form_sale":form_sale,
		"query_stock":query_stock,
		"page_sale":page_sale,
	}
  
  
	return render(request,'html_sale/sale.html',context)