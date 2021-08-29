from django.contrib.gis import admin

# Register your models here.
from .models import *

class StateInfoAdmin(admin.OSMGeoAdmin):
    list_display = ('state', 'census2010pop', 'popestimate2019')
    read_only = True
    map_height = 800
    map_width = 850
    ordering = ['state']
admin.site.register(StateInfo, StateInfoAdmin)


class CountyInfoAdmin(admin.OSMGeoAdmin):
    list_display = ('county', 'state', 'census2010pop', 'popestimate2019')
    list_filter = ('state', )
    read_only = True
    map_height = 800
    map_width = 850
    ordering = ['state', 'county']
admin.site.register(CountyInfo, CountyInfoAdmin)
