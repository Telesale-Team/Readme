from django.db import models

# Create your models here.
class Stock (models.Model):
    item = models.CharField(max_length=200)
    details = models.TextField(null=True,blank=True)
    serial = models.CharField(max_length=100)
    pgive = models.CharField(max_length=200)
    presive = models.CharField(max_length=100)
    created_dat = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.item
