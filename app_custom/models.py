from django.db import models
from app_team.models import *
from django.contrib.auth.models import User


# Create your models here.


class Cus(models.Model):
    
    userCus = models.CharField(max_length=255)
    passCus = models.CharField(max_length=255)
    telCus = models.CharField(max_length=255)
    buyUnit = models.IntegerField()
    idLine = models.CharField(max_length=255)
    namePage = models.CharField(max_length=255)
    registWeb = models.CharField(max_length=255)
    etc = models.TextField()
    
    def __str__(self) :
        return self.userCus
    

    
    