from django.urls import path,include

from .views import *


urlpatterns = [
    path('',applogin),
    path('register/',appregister),
    path('logout/',applogout),

    
]