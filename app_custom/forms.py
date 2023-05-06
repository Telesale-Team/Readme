from django import forms
from .models import *
from app_kpi.models import Customer_Interest

class ThaibanForm(forms.ModelForm):
    user_type = ('lable')

    class Meta:

        model = Customer_Interest
        fields = '__all__'