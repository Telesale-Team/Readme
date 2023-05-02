from django.db import models
from app_user.models import *
from django.contrib.auth.models import User


# Create your models here.



#ตัวอย่างการใช้งาน ManytoManyField
class Person(models.Model):
    name = models.CharField(max_length=128)
    
    
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Person"
        verbose_name = "Group & Team"

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through="Membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64,null=True)
    
    
    class Meta:
        ordering = ["id"]
        db_table = "Member"
        verbose_name_plural = "Membership"
        verbose_name = "Group & Team"
        
        
    def __str__(self):
        return f'{self.group} สมาชิก {self.person}'
    
    
