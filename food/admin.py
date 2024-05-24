from django.contrib import admin

from .models import Item
from .models import Order

# Register your models here.

admin.site.site_header = 'FoodApp Admin'
admin.site.site_title = 'FoodApp Admin'
admin.site.index_title = 'Welcome to FoodApp'
admin.site.register(Item)
admin.site.register(Order)
