from django import forms
from .models import *

class ProfileForm(forms.ModelForm):

    class Meta:

        model = ProfileUser
        fields = '__all__'
        
class SkillForm(forms.ModelForm):

    class Meta:

        model = Skill
        fields = '__all__'
        
class TeamForm(forms.ModelForm):

    class Meta:

        model = Team
        fields = '__all__'
        
class IdForm(forms.ModelForm):

    class Meta:

        model = Positions
        fields = '__all__'