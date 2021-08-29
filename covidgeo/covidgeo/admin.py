from django.contrib.gis import admin

# Register your models here.
from .models import *

class CountyInfoAdmin(admin.OSMGeoAdmin):
    list_display = ('county', 'state', 'popestimate2019')
    list_filter = ('state', )
    read_only = True
    map_height = 800
    map_width = 850
    ordering = ['state', 'county']
admin.site.register(CountyInfo, CountyInfoAdmin)
