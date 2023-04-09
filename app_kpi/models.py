from django.db import models
from app_team.models import Team
from app_user.models import ProfileUser
from app_money.models import *
from django.utils import timezone




class Kpi (models.Model):

    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    name = models.ForeignKey(ProfileUser,on_delete=models.CASCADE)
    new_customer = models.IntegerField(default=0)   #ลูกค้าใหม่
    slakthai = models.IntegerField(default=0) # สลากไท
    mughuay = models.IntegerField(default=0) # มักหวย
    member = models.IntegerField(default=0)  #`จำนวนสมาชิก`
    pay = models.IntegerField(default=0)     #`รายจ่าย`
    income = models.IntegerField(default=0) #รายได้
    profit = models.IntegerField(default=0) #`กำไร`
    created = models.DateTimeField(default=timezone.now) #วันที่

    def __str__(self):
        return str(self.created)+" "+str(self.team)
    
