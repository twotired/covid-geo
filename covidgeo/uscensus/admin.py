from django.contrib import admin

from .models import *

# Register your models here.

class PopulationAdmin(admin.ModelAdmin):
    list_display = ['stname', 'ctyname', 'popestimate2019', 'popestimate2020']
    list_filter = ['stname']
    ordering = ['stname', 'ctyname']
admin.site.register(Population, PopulationAdmin)
