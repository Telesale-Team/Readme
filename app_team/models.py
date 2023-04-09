from django.db import models
from app_user.models import *
from django.contrib.auth.models import User


# Create your models here.
class Team (models.Model):
    team = models.CharField(max_length=100,unique=True)
    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.team
    
