from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Category (models.Model):
    
    name = models.CharField(max_length=60)
    class Meta:

        verbose_name_plural = "Create Category"
        verbose_name = "Category"
    
    def __str__(self) :
        return self.name
    
    
class Item (models.Model):
    
    name = models.CharField('ชื่อไอเท็ม',max_length=60)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True) 
    serial = models.CharField(max_length=60)
    qutity = models.PositiveIntegerField(null=True)
    
    class Meta:
        db_table = "Item"
        verbose_name_plural = "Create Item"
        verbose_name = "Item"
    

    def __str__(self) :
        return self.name

class Stock (models.Model):
    
    item = models.ForeignKey(Item,on_delete=models.CASCADE,null=True)   
    quatity = models.PositiveIntegerField(default=1)
    user_account = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    date = models.DateField()
    
    class Meta:

        verbose_name_plural = "Stock"
        verbose_name = "Item"

    def __str__(self):
        return f'{self.item} by {self.user_account}'



#การใช้งาน Choices Modals
class Runner(models.Model):
    
    MedalType = models.TextChoices("MedalType", "GOLD SILVER BRONZE")
    name = models.CharField("person's first name",max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)
    

    def __str__(self):
        return self.name


