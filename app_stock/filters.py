import django_filters
from .models import *

class StockFilter(django_filters.FilterSet):

    class Meta:
        model = Stock
        fields = {

                'serial':['icontains'],
                'name':['icontains'],
                'detail':['icontains'],
                'category':['exact'],
                'user_account':['exact'],
                
                  }

