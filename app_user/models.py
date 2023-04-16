from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class ProfileUser(models.Model):
    
    create = models.DateTimeField(auto_now_add=True,null=True,blank=True) #วันเริ่มงาน
    username = models.OneToOneField(User,on_delete=models.CASCADE) #Id Login System
    id_user = models.IntegerField(default=0000,blank=True)	# รหัสพนักงาน
    nickname = models.CharField(max_length=20,blank=True)	# ชื่อเล่น
    team = models.CharField(max_length = 100,default='member') #สังกัดทีม
    image = models.ImageField(upload_to='image_profile',null=True,blank=True,default='default.png') #รูปถ่าย
    position = models.CharField(max_length=60,blank=True) # ตำแหน่งงาน
    age = models.IntegerField(default=0,blank=True) # อายุ
    sorary = models.IntegerField(default=9000) #เงินเดือน
    dayofwork = models.IntegerField(default=0) #วันทำงาน
    ot = models.IntegerField(default=0) # ot
    bonus = models.IntegerField(default=0)# Bonus
    worklate = models.IntegerField(default=0) #มาสาย
    sick = models.IntegerField(default=0) # ลาป่วย
    la = models.IntegerField(default=0) # ลากิจ
    leave = models.IntegerField(default=0) # ขาด
    money_advance= models.IntegerField(default=0) # เบิกล่วงหน้า
    money_food = models.IntegerField(default=0) #ค่าอาหาร
    money_home = models.IntegerField(default=0) #ค่าบ้าน
    money_traff = models.IntegerField(default=0)  #ค่าเดินทาง 
    
    
    def __str__ (self):
        return str(self.username)
    
    
