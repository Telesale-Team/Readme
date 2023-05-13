from django import forms
from .models import *

class StockForm(forms.ModelForm):
    class Meta:

        model = Stock
        fields = '__all__'
        
        
        
class CategoryForm(forms.ModelForm):

    class Meta:

        model = Category
        fields = '__all__'
        
        
class ItemFrom(forms.ModelForm):

    class Meta:

        model = Notebook
        fields = '__all__'


class CableForm(forms.ModelForm):

    class Meta:

        model = Cable
        fields = '__all__'
        
class NotebookForm(forms.ModelForm):

    class Meta:

        model = Notebook
        fields = '__all__'
        
        
class OfficeForm(forms.ModelForm):
    class Meta:

        model = Office
        fields = '__all__'
        