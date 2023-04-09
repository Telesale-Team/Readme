from django.urls import path,include

from .views import *


urlpatterns = [
    path('',index),
    path('add_dashbaord/',Add_dashboard,name='adddashboard' ),
    path('dashboard/',Dashboard,name='dashboard' ),
 
    
]
