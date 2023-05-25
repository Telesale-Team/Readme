from django import forms
from .models import *
from django.core.validators import RegexValidator

class StockForm(forms.ModelForm):
    name = forms.CharField(
        label='ชื่อสินค้า',min_length=3, max_length=50, required=True,
        widget=forms.TextInput(attrs={'placeholder':'เช่น Lenovo Ideapad 3... '})
        )
    
    class Meta:

        model = Stock
        fields = '__all__'
        
        
        
class CategoryForm(forms.ModelForm):

    class Meta:

        model = Category
        fields = '__all__'
        
        

        