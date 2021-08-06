from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(US, admin.ModelAdmin)

class StateAdmin(admin.ModelAdmin):
    list_display = ('date', 'state', 'fips', 'cases', 'deaths')
    list_filter = ('state', 'fips')
    read_only = True
admin.site.register(State, StateAdmin)

class CountyAdmin(admin.ModelAdmin):
    list_display = ('date', 'state', 'county', 'fips', 'cases', 'deaths')
    list_filter = ('state', 'county')
admin.site.register(County, CountyAdmin)
