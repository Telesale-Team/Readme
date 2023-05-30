from django.urls import path,include
from app_user.views import *
from .views import *
urlpatterns = [
	path('',Index,name="sale-home"),
 
	

]