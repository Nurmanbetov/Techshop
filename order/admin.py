from django.contrib import admin
from .models import *


class ProductInOrderInLine(admin.StackInline):
    model = ProductInOrder
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order

    list_display = ["name", "phone", "get_product_count"]
    inlines = [
        ProductInOrderInLine
    ]

    def get_product_count(self, obj):
        return obj.product_in_order.count()



@admin.register(ProductInOrder)
class ProductInOrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ("order", "product", "added")
    readonly_fields = ("order", "product", "added")
