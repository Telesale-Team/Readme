from django.urls import path,include
from .views import *
from app_user.views import *


urlpatterns = [
    
    path('',Dashboard,name='profileuser'),
    path('add_user/',Add_user,name='adduser'),
    path('add_position/',Add_Position),
    path('add_team/',Add_Team),
    path('add_skill/',Add_Skill),
   
    path('delete_user/',Delete_user),
    path('edit_user/',Edit_user),
    path('report_user/',Report_user),
    path('profile/<int:id>',Profile),
     path('profile_update/<int:id>',Update_user),
    
    
    
]