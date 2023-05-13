from django.shortcuts import render,redirect
from django.http import HttpResponse
from app_user.models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ProfileUser
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url="/")
def PositionGroup (request,position=None):

    if position != None:
        position = get_object_or_404(Positions,name=position)
        position = ProfileUser.objects.all().filter(position=position)
        
    else:
        position = ProfileUser.objects.all()
        
    context = {
        "postion":position
    }
        
    return render(request,'html_user/position_group.html',context)


@login_required(login_url='/')
def Dashboard (request,position_slug=None):

    profileCheck = ProfileUser.objects.all().filter(image_check=False)

    if position_slug != None:
        profile = ProfileUser.objects.all()
        
    else:
        profile = ProfileUser.objects.all().filter(image_check=False)
        

    profile_unit = list(profile)
    total = len(profile_unit)
    
    context = {

        "profile_unit":len(profile_unit),
        "profile":profile,
        "total":total,
        "profileCheck":profileCheck,
    }
    
    return render (request,'html_user/dashboard_user.html',context)


@login_required(login_url="/")
def Profile (request,pk ):
    
    user = ProfileUser.objects.get( pk = pk )

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

    return render (request,'html_user/profile_user.html',context)


@login_required
def delete_profile(request, pk):
    user_profile = get_object_or_404(ProfileUser, pk=pk)
    


    if request.method == 'POST':
        user_profile.delete()
        return redirect('/user') 
    else:
        return render(request, 'html_login/delete_profile.html', {'user_profile': user_profile})

def Update_profile (request,pk):
    profile = ProfileUser.objects.get(pk=pk)
    if request.method == 'POST':
        profile_form= ProfileForm(request.POST,request.FILES,instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('/user')

    else:
        profile_form= ProfileForm(instance=profile)

    context = {

        "profile_form":profile_form,
        "profile":profile
    }
    return render(request, 'html_login/update-profile.html', context)


@login_required(login_url="/")
def Add_Position (request ):
    
    user = ProfileUser.objects.all()
    position = Positions.objects.all()

    if request.method == "POST":
        form = IdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/customer")
    else:
        form = IdForm()
        
        
    context = {
        "user":user,
        "position":position,
		"form": form,
	}

    return render (request,'html_user/add_positions.html',context)





@login_required(login_url="/")
def Add_Team (request ):
    
    team = Team.objects.all()

    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/user")
    else:
        form = TeamForm()
        
        
    context = {
        "team":team,
		"form": form,

	}

    return render (request,'html_user/add_team.html',context)


@login_required(login_url="/")
def Add_Skill (request ):
    
    skill = Skill.objects.all()
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/user")
    else:
        form = SkillForm()
        
        
    context = {

		"form": form,
        "skill": skill,

	}

    return render (request,'html_user/add_skill.html',context)


@login_required(login_url="/")
def Report_user (request):
    return render(request,'html_user/report_user.html')


@login_required(login_url="/")
def Hr (request):
    return render(request,'html_user/hr.html')

@login_required(login_url="/")
def At (request):
    return render(request,'html_user/at.html')


@login_required(login_url="/")
def Mt (request):
    return render(request,'html_user/mt.html')

@login_required(login_url="/")
def St (request):
    return render(request,'html_user/st.html')

@login_required(login_url="/")
def Ad (request):
    return render(request,'html_user/ad.html')


@login_required(login_url="/")
def It (request):
    
    user = ProfileUser.objects.all()
    context = {
        "user":user,
	}

    return render(request,'html_user/it.html',context)