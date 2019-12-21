from django.contrib import admin
from .models import All_notebook_product_page, Order, OrderItem

# Register your models here.

admin.site.register(All_notebook_product_page)
admin.site.register(Order)
admin.site.register(OrderItem)
