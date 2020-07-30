from django.contrib import admin
from .models import *


class ProductInOrderInLine(admin.TabularInline):
    model = ProductInOrder
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [
        ProductInOrderInLine
    ]

# Register your models here.
