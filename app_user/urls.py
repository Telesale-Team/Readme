from django.urls import path,include
from .views import *
from app_user.views import *


urlpatterns = [
    
    path('',Dashboard,name='profileuser'),
    path('add_user/',Add_user,name='adduser'),
    path('update_user/',Update_user,name='updateuser'),
    path('delete_user/',Delete_user,name='deleteuser'),
    path('edit_user/',Edit_user,name='edituser'),
    path('report_user/',Report_user,name='reportuser'),
    path('profile/<int:id_user>',Profile,name='profile'),
    
    
    
]