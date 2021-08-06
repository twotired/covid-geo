from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import *

mapping = {
    'uace10': 'UACE10',
    'geoid10': 'GEOID10',
    'name10': 'NAME10',
    'namelsad10': 'NAMELSAD10',
    'lsad10': 'LSAD10',
    'mtfcc10': 'MTFCC10',
    'uatyp10': 'UATYP10',
    'funcstat10': 'FUNCSTAT10',
    'aland10': 'ALAND10',
    'awater10': 'AWATER10',
    'intptlat10': 'INTPTLAT10',
    'intptlon10': 'INTPTLON10',
    'geom': 'MULTIPOLYGON',
}

shp_path = '/data/tl_2020_us_uac10.shp'

def run(shp_path=shp_path, verbose=True):
    lm = LayerMapping(UrbanArea, shp_path, mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

# from tiger import load_urbanareas ; load_urbanareas.run()
