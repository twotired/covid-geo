from django.contrib.gis import admin

# Register your models here.
from .models import State

admin.site.register(State, admin.GeoModelAdmin)
