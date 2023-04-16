from django.urls import path,include

from .views import *


urlpatterns = [

    path('add_dashbaord/',Add_dashboard ),
    path('',Dashboard,name='dashboard' ),
 
    
]
