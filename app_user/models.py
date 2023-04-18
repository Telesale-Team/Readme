from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class ProfileUser(models.Model):
    
    create_date = models.DateTimeField(auto_now_add=True,null=True,blank=True) #วันเริ่มงาน
    id_user = models.IntegerField(default=0000,blank=True)	# รหัสพนักงาน
    lastname = models.CharField(max_length=255,blank=True,null=True)
    username = models.OneToOneField(User,on_delete=models.CASCADE) # ชื่อพนักงาน    
    nickname = models.CharField(max_length=20,blank=True)	# ชื่อเล่นพนักงาน
    email = models.EmailField(max_length=100,blank=True,null=True) # อีเมลล์
    address = models.CharField(max_length=255,blank=True,null=True)# ที่อยู่ 
    num_phone = models.CharField(max_length=10,blank=True,null=True) #  เบอร์โทรศัพท์
    image = models.ImageField(upload_to='image_profile',null=True,blank=True,default='default.png') #รูปถ่าย
    position = models.CharField(max_length=60,blank=True,null=True) # ตำแหน่งงาน
    worked = models.TextField(blank=True,null=True) # ประวัติการทำงาน
    talen = models.TextField(blank=True,null=True) # ความถนัด

    def __str__ (self):
        return str(self.username)
    
    
