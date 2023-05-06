from django import forms
from .models import *

class KipForm(forms.ModelForm):

    class Meta:

        model = Dashboard
        fields = '__all__'
        
        
class ThaibanForm(forms.ModelForm):

    class Meta:

        model = Customer_Interest
        fields = '__all__'