from django.urls import path,include

from .views import *


urlpatterns = [
    path('',dashboard,name='stock'),
    path('add_stock',Add_stock),
    path('add_Category/',Add_Category),
    path('add_Item/',Add_Item),
]