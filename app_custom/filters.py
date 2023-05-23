import django_filters
from .models import *

class NotebookFilter(django_filters.FilterSet):

    class Meta:
        model = Cus
        fields = {
            'userCus':['exact'],
            
            }
        
        