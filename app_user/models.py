from django.db import models
from django.contrib.auth.models import User




# Create your models here.

class Positions (models.Model):
    name = models.CharField(max_length=255,unique=True)
    
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Create Position"
        verbose_name = "Name Position"
    
    def __str__(self):
        return self.name

class Skill (models.Model):
    name = models.CharField(max_length=255,unique=True)
    
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Create Skill"
        verbose_name = "Name Skill"
    
    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.name
    
class Team (models.Model):
    name = models.CharField(max_length=255)
    team =  models.ImageField(upload_to='image_teams',null=True,blank=True,default='default.png') #รูปถ่าย
    detail = models.CharField(max_length=255)
    
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Create Team"
        verbose_name = "Name Team"
    
    def __str__(self):
        return self.name


class ProfileUser(models.Model):
    
    username = models.OneToOneField(User,on_delete=models.CASCADE) # ชื่อพนักงาน  
    nickname = models.CharField(max_length=20,blank=True)	# ชื่อเล่นพนักงาน
    address = models.CharField(max_length=255,blank=True,null=True)# ที่อยู่ 
    phone = models.CharField(max_length=10,unique=True,blank=True) #  เบอร์โทรศัพท์
    image = models.ImageField(upload_to='image_profile',null=True,blank=True,default='default.png') #รูปถ่าย
    position = models.ForeignKey(Positions,on_delete=models.CASCADE,blank=True,null=True)
    team = models.ForeignKey(Team,on_delete=models.CASCADE,blank=True,null=True)
    MedalType = models.TextChoices("MedalType", "ต่ำกว่า1ปี 1ปี 2ปี มากกว่า3ปี")
    working_experience = models.CharField(blank=True, choices=MedalType.choices, max_length=10)
    working_skill = models.ForeignKey(Skill,on_delete=models.CASCADE,blank=True,null=True)
    worked_date = models.DateField()


    
    class Meta:
        ordering = ["-username"]
        verbose_name_plural = "Profile"
        verbose_name = "Member"

    def __str__ (self):
        return str(self.username)
    

