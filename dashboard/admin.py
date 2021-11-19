from django.contrib import admin
from .models import Bot_location, Map

class Bot_locationAdmin(admin.ModelAdmin):
    list_display = ['bot', 'x', 'y', 'angle']

admin.site.register(Bot_location, Bot_locationAdmin)
admin.site.register(Map)
# Register your models here.

