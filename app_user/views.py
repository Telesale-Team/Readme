from django.shortcuts import render,redirect
from django.http import HttpResponse
from app_user.models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/')
def Dashboard (request):

    users = User.objects.all().order_by('-username')
    profile = ProfileUser.objects.all().order_by('-username')
    user_unit = list(users)
    profile_unit = list(profile)
    total = len(profile_unit)
    
    context = {
        "quatity":len(user_unit),
        "profile_unit":len(profile_unit),
        "profile":profile,
        "users":users,
        "total":total,



    }
    
    return render (request,'html_user/dashboard_user.html',context)




@login_required(login_url="/")
def Add_user (request):
    
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/user")
    else:
        form = ProfileForm()

        
            
    context = {

        "form": form


    }
    
    return render(request,'html_user/add_user.html',context)




@login_required(login_url="/")
def Add_Position (request ):
    
    user = ProfileUser.objects.all()

    if request.method == "POST":
        form = IdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/customer")
    else:
        form = IdForm()
        
        
    context = {
        "user":user,
		"form": form,
	}

    return render (request,'html_user/add_positions.html',context)





@login_required(login_url="/")
def Add_Team (request ):
    
    user = Team.objects.all()

    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/user")
    else:
        form = TeamForm()
        
        
    context = {
        "user":user,
		"form": form,

	}

    return render (request,'html_user/add_team.html',context)



@login_required(login_url="/")
def Add_Skill (request ):
    
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/user")
    else:
        form = SkillForm()
        
        
    context = {

		"form": form,

	}

    return render (request,'html_user/add_skill.html',context)



@login_required(login_url="/")
def Profile (request,id ):
    
    user = ProfileUser.objects.get( id = id )

    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/customer")
    else:
        form = ProfileForm(instance=user)
        
        
    context = {
        "user":user,
		"form": form,
	}

    return render (request,'html_user/profile_user.html',context)





@login_required(login_url="/")
def Delete_user (request):
    
    return render(request,'html_user/delete_user.html')



@login_required(login_url="/")
def Update_user(request,id):
    
    user = ProfileUser.objects.get(id = id)
    if request.method == "POST":
        form = ProfileForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect("/user")
    else:
        form = ProfileForm(instance=user)
        
        
    context = {
        "user":user,
		"form": form,
	}

    return render(request,'html_user/profile_user.html',context)



@login_required(login_url="/")
def Edit_user (request):
    
    
    return render(request,'html_user/edit_user.html')

@login_required(login_url="/")
def Report_user (request):
    return render(request,'html_user/report_user.html')