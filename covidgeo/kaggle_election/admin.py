from django.contrib import admin

from .models import *

# Register your models here.

class PresidentCounty2020Admin(admin.ModelAdmin):
    list_display = ['state', 'county', 'candidate', 'party', 'total_votes', 'won']
    list_filter = ('state', 'won', 'candidate')
    read_only = True
    ordering = ['state', 'county', 'won', 'total_votes']
admin.site.register(PresidentCounty2020, PresidentCounty2020Admin)
