from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category (models.Model):
    
    name = models.CharField('ชื่อหมวดหมู่',max_length=60)
    class Meta:

        verbose_name_plural = "Create Category"
        verbose_name = "Category"
    
    def __str__(self) :
        return self.name
    

    
class Stock (models.Model):
    
    name = models.CharField('ชื่อสินค้า',max_length=60,null=True)
    serial = models.CharField("รหัสสินค้า",max_length=60,null=True)
    quatity = models.PositiveIntegerField('จำนวน',default=0)
    detail = models.TextField('อุปกรณ์เสริม',max_length=255,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    user_account = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    date = models.DateField('วันที่',)
    
    class Meta:

        verbose_name_plural = "Create Cable"
        verbose_name = "Item"

    def __str__(self):
        return f'{self.name} by {self.user_account}'
    

#การใช้งาน Choices Modals
class Runner(models.Model):
    
    MedalType = models.TextChoices("MedalType", "GOLD SILVER BRONZE")
    name = models.CharField("person's first name",max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)
    

    def __str__(self):
        return self.name


