from django.shortcuts import render,redirect
from django.http import HttpResponse
from app_user.models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .filters import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator
# Create your views here.

@login_required(login_url='/')
def Dashboard (request):
	profile = ProfileUser.objects.all()
	alluser = profile.count
	
	page = Paginator(profile,5)
	page_list = request.GET.get("page")
	page = page.get_page(page_list)
 
	user_filter = ProfileFilter(request.GET,queryset=ProfileUser.objects.all())
	filter = user_filter.form
	user = user_filter.qs

	
	context = {

		"filter": filter,
		"user":user,
		"alluser":alluser,
		"page" : page,
  
	
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
	return render(request, 'html_user/update-profile.html', context)

@login_required
def Delete_profile(request,pk):
	
	user = get_object_or_404(ProfileUser, pk = pk)
	
	if request.method == 'POST':
		user.delete()
		return redirect('/user')  # Redirect to home page or any other appropriate page
	else:
		return render(request, 'html_user/delete_profile.html', {'user': user})

@login_required(login_url="/")
def Add_Position (request ):

	position_filter = PositionFilter(request.GET,queryset=Positions.objects.all())
	filter = position_filter.form
	position = position_filter.qs
 
	if request.method == "POST":
		form = PositionForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/user/add_position/")
	else:
		form = PositionForm()
		
		
	context = {

		"position":position,
		"form": form,
		"position_filter":position_filter,
		"filter":filter,
	}

	return render (request,'html_user/add_positions.html',context)

@login_required(login_url="/")
def Update_Position (request,id ):
	

	position = get_object_or_404(Positions, id=id)

	if request.method == "POST":
		form = PositionForm(request.POST,instance=position)
		if form.is_valid():
			form.save()
			return redirect("/user/add_position")
	else:
		form = PositionForm(instance=position)
		
		
	context = {

		"position":position,
		"form": form,
	}

	return render (request,'html_user/update_positions.html',context)

@login_required
def Delete_Position(request, id):
	position = get_object_or_404(Positions, id=id)

	if request.method == 'POST':
		position.delete()
		return redirect("/user/add_position")  # Redirect to home page or any other appropriate page
	else:
		return render(request, 'html_user/delete_positions.html', {'position': position})


@login_required(login_url="/")
def Add_Team (request ):
	

	filterteam = TeamFilter(request.GET,queryset=Team.objects.all())
	filter = filterteam.form
	team = filterteam.qs
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
		"filter":filter,

	}

	return render (request,'html_user/add_team.html',context)

@login_required(login_url="/")
def Update_Team (request,pk ):
	

	team = get_object_or_404(Team, pk=pk)

	if request.method == "POST":
		form = TeamForm(request.POST,request.FILES,instance=team)
		if form.is_valid():
			form.save()
			return redirect("/user/add_team/")
	else:
		form = TeamForm(instance=team)
		
		
	context = {

		"team":team,
		"form": form,
	}

	return render (request,'html_user/update_team.html',context)


@login_required
def Delete_Team(request,pk):
	
	team = get_object_or_404(Team, pk = pk)
	
	if request.method == 'POST':
		team.delete()
		return redirect('/user/add_team/')  # Redirect to home page or any other appropriate page
	else:
		return render(request, 'html_user/delete_team.html', {'team': team})


@login_required(login_url="/")
def Add_Skill (request ):
	

	filterskill = SkillFilter(request.GET,queryset=Skill.objects.all())
	filter = filterskill.form
	skill = filterskill.qs
 
	if request.method == "POST":
		form = SkillForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/user/add_skill/")
	else:
		form = SkillForm()
		
		
	context = {

		"form": form,
		"skill": skill,
		"filter":filter,

	}

	return render (request,'html_user/add_skill.html',context)

@login_required(login_url="/")
def Update_Skill (request,pk ):
	

	skill = get_object_or_404(Skill, pk=pk)

	if request.method == "POST":
		form = SkillForm(request.POST,request.FILES,instance=skill)
		if form.is_valid():
			form.save()
			return redirect("/user/add_skill/")
	else:
		form = SkillForm(instance=skill)
		
		
	context = {

		"skill":skill,
		"form": form,
	}

	return render (request,'html_user/update_skill.html',context)


@login_required
def Delete_Skill(request,pk):
	
	skill = get_object_or_404(Skill, pk = pk)

	if request.method == 'POST':
		skill.delete()
		return redirect('/user/add_skill/')  # Redirect to home page or any other appropriate page
	else:
		return render(request, 'html_user/delete_skill.html', {'skill': skill})





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