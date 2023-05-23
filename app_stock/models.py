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
    
class Notebook (models.Model):
    
    username = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True) 
    name = models.CharField('ชื่อสินค้า',max_length=60)
    user_login = models.CharField("ชื่อล็อคอิน",max_length=60,null=True)
    password_login = models.CharField("รหัสล็อคอิน",max_length=60,null=True)
    serial = models.CharField("รหัสสินค้า",max_length=60,null=True)
    serial2 = models.CharField("หมายเลขประจำเครื่อง",max_length=60,null=True)
    mouse = models.BooleanField('เม้าส์',default=True)
    name_mouse = models.CharField("ยี่ห้อเม้าส์",max_length=60,null=True)
    mouse_mat = models.BooleanField('แผ่นรองเม้า',default=True)
    name_mouse_mat = models.CharField("ชื่อแผ่นรองเม้าส์",max_length=60,null=True)
    image = models.ImageField('อัพโหลดภาพหลักฐาน',upload_to='image_notebook',default='default.jpg',blank=True)
    date = models.DateField(auto_now_add=True,null=True)
    

    
    class Meta:
        db_table = "Item"
        verbose_name_plural = "Create Notebook"
        verbose_name = "Item"
    

    def __str__(self) :
        return f"{self.name} by {self.username}" 
    
class Cable (models.Model):
    
    name = models.CharField('ชื่อสินค้า',max_length=60,null=True)
    serial = models.CharField("รหัสสินค้า",max_length=60,null=True)
    quatity = models.PositiveIntegerField('จำนวน',default=1)
    detail = models.TextField('อุปกรณ์เสริม',max_length=255,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    user_account = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    date = models.DateField('วันที่',)
    
    class Meta:

        verbose_name_plural = "Create Cable"
        verbose_name = "Item"

    def __str__(self):
        return f'{self.name} by {self.user_account}'
    
class Office (models.Model):
    user_account = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True) 
    item_name = models.CharField('ชื่อสินค้า',max_length=60,null=True)  
    quatity = models.PositiveIntegerField('จำนวน',default=0)
    detail = models.TextField('รายละเอียดเพิ่มเติม',max_length=255,null=True)
    date = models.DateField()
    
    class Meta:

        verbose_name_plural = "Create Office"
        verbose_name = "Item"

    def __str__(self):
        return f'{self.item_name} by {self.user_account}'

class Stock (models.Model):
    
    item = models.ForeignKey(Notebook,on_delete=models.CASCADE,null=True)   
    quatity = models.PositiveIntegerField(default=0)
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


