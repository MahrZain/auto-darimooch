from django.contrib import admin
from.models import nav
# Register your models here.

class NavAdmin(admin.ModelAdmin):
    list_display = ['menu','url']
    # list_editable = ('order',)
admin.site.register(nav,NavAdmin)