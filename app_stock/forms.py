from django import forms
from .models import *

class StockForm(forms.ModelForm):
    date = forms.DateTimeField()
    class Meta:

        model = Stock
        fields = '__all__'
        
        
        
class CategoryForm(forms.ModelForm):

    class Meta:

        model = Category
        fields = '__all__'
        
        
class ItemFrom(forms.ModelForm):

    class Meta:

        model = Item
        fields = '__all__'