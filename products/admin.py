from django.contrib import admin
from .models import products


# Register your models here.
class productsAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "price",
        "sale",
        "total_amount_products",
        "image",
        "cat_id",
    ]


admin.site.register(products, productsAdmin)
