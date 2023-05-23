from django.urls import path,include

from .views import *


urlpatterns = [
    path('',dashboard,name='stock'),
    path('add_stock',Add_stock,name="add-stock"),
    
    
    path('add_stock/add_cable',Add_Cable,name='add-cable'),
    
    
    path('add_stock/add_notebook',Add_Notebook,name="add-notebook"),
    
    
    path('add_stock/add_office',Add_Office,name="add-office"),
    path('add_Category/',Add_Category,name="add_Category"),
    path('add_Item/',Add_Item),
    

    path('pickup_notebook/<int:id>',Pickup,name='pickup_notebook'),

    
]