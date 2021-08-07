from django.contrib.gis import admin

# Register your models here.
from .models import *

class StateAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'stusps', 'region')
    list_filter = ('region', )
    read_only = True
    map_height = 800
    map_width = 850
    ordering = ['name']
admin.site.register(State, StateAdmin)

class CountyAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'statefp')
    list_filter = ('statefp', )
    read_only = True
    map_height = 800
    map_width = 850
    ordering = ['statefp', 'namelsad']
admin.site.register(County, CountyAdmin)

class UrbanAreaAdmin(admin.OSMGeoAdmin):
    list_display = ('name10', 'uace10', 'lsad10')
    list_filter = ('uace10', 'lsad10')
    read_only = True
    map_height = 800
    map_width = 850
    ordering = ['name10']
admin.site.register(UrbanArea, UrbanAreaAdmin)

class CongressionalDistrictAdmin(admin.OSMGeoAdmin):
    list_display = ('cd116fp', 'namelsad', 'statefp')
    list_filter = ('statefp', )
    read_only = True
    map_height = 800
    map_width = 850
    ordering = ['statefp', 'namelsad']
admin.site.register(CongressionalDistrict, CongressionalDistrictAdmin)
