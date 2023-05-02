from django.contrib import admin
from .models import *

admin.site.register(Person)
admin.site.register(Membership)
admin.site.register(Group)