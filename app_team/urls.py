from django.urls import path
from .views import *

urlpatterns = [
    path('', team_list, name='team_list'),
    path('edit_team/', Edit_team,),
    path('delete_team/', Delete_team,),
    path('add_team/', Add_team,),
    path('search_team/', Search_team,),
    path('report_team/', Report_team,),
]
