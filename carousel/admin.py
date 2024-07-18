from django.contrib import admin
from .models import carousel

# Register your models here.


class CarouselAdmin(admin.ModelAdmin):
    list_display = ["title", "caption", "image"]


admin.site.register(carousel, CarouselAdmin)
