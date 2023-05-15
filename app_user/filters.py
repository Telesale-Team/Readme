import django_filters
from app_user.models import *

class ProfileFilter(django_filters.FilterSet):

    class Meta:
        model = ProfileUser
        fields = {'nickname':['icontains']}
        