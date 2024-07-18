from django.contrib import admin
from .models import Announcement
# Register your models here.

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['message', 'buy_now']
    
admin.site.register(Announcement , AnnouncementAdmin)

