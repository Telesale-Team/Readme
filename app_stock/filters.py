import django_filters
from .models import *

class NotebookFilter(django_filters.FilterSet):

    class Meta:
        model = Cable
        fields = {
                'serial':['iexact'],
                'name':['iexact'], 
                'category':['exact'],
                'user_account':['exact'],
                  }



class StockFilter(django_filters.FilterSet):

    class Meta:
        model = Stock
        fields = {'item':['exact'],

                  }
        