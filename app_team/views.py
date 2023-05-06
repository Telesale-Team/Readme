from django.shortcuts import render
from .models import *
from app_user.models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url="/")
def team_list(request):

    teams = Team.objects.all()
    

    return render (request,'html_team/team_dashboard.html',{"teams":teams})


@login_required(login_url="/")
def Edit_team(request):

  

    return render (request,'html_team/edit_team.html')


@login_required(login_url="/")
def Delete_team(request):

  

    return render (request,'html_team/delete_team.html')


@login_required(login_url="/")
def Add_team(request):

  

    return render (request,'html_team/add_team.html')



@login_required(login_url="/")
def Search_team(request):

  

    return render (request,'html_team/search_team.html')


@login_required(login_url="/")
def Report_team(request):

  

    return render (request,'html_team/report_team.html')

