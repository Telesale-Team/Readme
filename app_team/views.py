from django.shortcuts import render
from .models import *
from app_user.models import *
from django.http import HttpResponse

def team_list(request):

    teams = ProfileUser.objects.all()
    

    return render (request,'frontend/team_dashboard.html',{"teams":teams})