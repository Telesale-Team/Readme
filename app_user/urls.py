from django.urls import path,include
from app_user.views import *
from app_login.views import delete_profile

urlpatterns = [
    path('',Dashboard),
    
    path('category/<slug:position_slug>',Dashboard),

    path('add_position/',Add_Position,name='add-position'),
    path('position/<str:position>',PositionGroup,name='search-position'),
    path('add_team/',Add_Team,name='add-team'),
    path('add_skill/',Add_Skill,name='add-skill'),

       
    path('hr/',Hr,name='hr'),
    path('at/',At,name='at'),
    path('mt/',Mt,name='mt'),
    path('st/',St,name='st'),
    path('ad/',Ad,name='ad'),
    path('it/',It,name='it'),
    
    path('report_user/',Report_user),
    path('profile/update/<int:pk>/',Update_profile,name='profile-update'),
    #path('profile/update/<int:pk>/',Profile,name='profile-update'),
    path('profile/delete/<str:username>/', delete_profile, name='delete_profile'),
    
    
    
]