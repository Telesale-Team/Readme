from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MoneyFinance (models.Model):
    
    name = models.CharField(max_length=255)    
    presive = models.CharField(max_length=255,blank=True)
    pgitve = models.CharField(max_length=255,blank=True)
    money = models.IntegerField(default=0,blank=True)
    details = models.TextField(null=True,blank=True)
    created_dat = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    
    def __str__(self):
        return str(self.name)
    
    
class Sorary (models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    money = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.username)+' '+ str(self.money)