from django.contrib import admin
from .models import Event, EventImage

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'date',
        'description'
    ]

admin.site.register(Event, EventAdmin)

class EventImageAdmin(admin.ModelAdmin):
    list_display = [
        'event',
        'caption',
        'image'
    ]

admin.site.register(EventImage, EventImageAdmin)
