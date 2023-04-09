from django.urls import path,include
from app_kpi.models import *

from .views import *


urlpatterns = [
    path('',dashboard),
    path('add_money/',Add_money),
    path('edit_money/',Edit_money,name='edit_money'),
    path('update_money/',Update_money,name='update_money'),
    path('delete_money/',Delete_money,name='delete_money'),
    path('search_money/',Search_money,name='search_money'),
    
    

    
]