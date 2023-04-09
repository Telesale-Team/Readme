from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.

def applogin (request):
	return render(request,'loginfile/login.html')

			

def appregister (request):
	
	if request.method == "POST":
			   
		# รับค่าจาก html
		
		username = request.POST["username"]
		email = request.POST["email"]
		password = request.POST["password"]
		repassword = request.POST["repassword"]
		
		if username == '' or email == '' or password == '' or repassword == '':
			messages.info(request,'กรุณากรอกข้อมูลให้ครบถ้วน !!!')                   
			return redirect('/login')
		
		elif password != repassword:
			messages.info(request,'  !!!')                   
			return redirect('/login')
		
		elif User.objects.filter(email=email).exists():
			messages.info(request,'email นี้มีในระบบแล้ว !!!')                   
			return redirect('/login')
						
			
		else:
			if User.objects.filter(username=username).exists():
				messages.info(request,'username นี้มีในระบบแล้ว !!!')
				return redirect('/login')
				
			else:
				newuser = User.objects.create_user(
					username=username,
					password=password,
					email=email
				)
				
				newuser.save()            
				messages.info(request,'ยินดีต้อนรับเข้าสู่การใช้งาน สมัครสมาชิกใช้งานเรียบร้อย')                   
				return redirect('/login/')
		
	return render(request,'loginfile/register.html')


def applogout (request):
	return render(request,'loginfile/logout.html')