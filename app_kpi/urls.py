from django.urls import path,include

from .views import *


urlpatterns = [
    path('',Dashboards,name='dashboard' ),
    path('add_dashbaord/',Add_dashboard ),
    path('thaiban/',Thaibans ),

]
