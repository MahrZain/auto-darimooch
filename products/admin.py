from django.contrib import admin
from .models import products


# Register your models here.
class productsAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "price",
        "category",
        "sale",
        "total_amount_products",
        "image"
    ]


admin.site.register(products, productsAdmin)
