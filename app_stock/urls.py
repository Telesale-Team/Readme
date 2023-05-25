from django.urls import path,include

from .views import *


urlpatterns = [
    path('',dashboard,name='stock'),
    path('update/<int:pk>',Update_Stock,name="update-stock"),
    path('delete/<int:pk>',Delete_Stock,name="delete-stock"),
    path('add_Category/',Add_Category,name="add_Category"),
     
]