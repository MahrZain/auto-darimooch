from django.contrib import admin
from .models import limage
from django.db import models

# Register your models here.


class LogoAdmin(admin.ModelAdmin):
    list_display = ["image"]


admin.site.register(limage, LogoAdmin)
