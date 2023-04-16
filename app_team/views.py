from django.shortcuts import render
from .models import *
from app_user.models import *
from django.http import HttpResponse

def team_list(request):

    teams = ProfileUser.objects.all()    

    return render (request,'html_team/team_dashboard.html',{"teams":teams})

def Edit_team(request):

  

    return render (request,'html_team/edit_team.html')

def Delete_team(request):

  

    return render (request,'html_team/delete_team.html')

def Add_team(request):

  

    return render (request,'html_team/add_team.html')


def Search_team(request):

  

    return render (request,'html_team/search_team.html')


def Report_team(request):

  

    return render (request,'html_team/report_team.html')

