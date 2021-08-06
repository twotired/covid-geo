from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import *

mapping = {
    'statefp': 'STATEFP',
    'cd116fp': 'CD116FP',
    'geoid': 'GEOID',
    'namelsad': 'NAMELSAD',
    'lsad': 'LSAD',
    'cdsessn': 'CDSESSN',
    'mtfcc': 'MTFCC',
    'funcstat': 'FUNCSTAT',
    'aland': 'ALAND',
    'awater': 'AWATER',
    'intptlat': 'INTPTLAT',
    'intptlon': 'INTPTLON',
    'geom': 'MULTIPOLYGON',
}

shp_path = '/data/tl_2020_us_cd116.shp'

def run(verbose=True):
    lm = LayerMapping(CongressionalDistrict, shp_path, mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

# from tiger import load_contressionaldistricts ; load_contressionaldistricts.run()
