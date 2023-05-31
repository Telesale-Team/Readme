import django_filters
from .models import *

class SaleFilter(django_filters.FilterSet):

    class Meta:
        model = Sale
        fields = {
            "name":['icontains'],
            "interest":['exact'],
            "sex":['exact'],
            "buy":['exact'],
    }