from django.contrib import admin
from .models import banner

class BannerAdmin(admin.ModelAdmin):
    list_display = ["image"]

admin.site.register(banner, BannerAdmin)
