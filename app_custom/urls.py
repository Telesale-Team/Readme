from django.urls import path,include

from .views import *


urlpatterns = [
    path('',index),
    path('add_custom/',Add_custom,name='addcustom'),
    path('update_custom/',Update_custom,name='updatecustom'),
    path('delete_custom/',Delete_custom,name='deletecustom'),
    path('edit_custom/',Edit_custom,name='editcustom'),
    path('report_custom/',Report_custom,name='reportcustom'),
    
 
    
]