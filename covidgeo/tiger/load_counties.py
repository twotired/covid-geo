from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import County

mapping = {
    'statefp': 'STATEFP',
    'countyfp': 'COUNTYFP',
    'countyns': 'COUNTYNS',
    'geoid': 'GEOID',
    'name': 'NAME',
    'namelsad': 'NAMELSAD',
    'lsad': 'LSAD',
    'classfp': 'CLASSFP',
    'mtfcc': 'MTFCC',
    'csafp': 'CSAFP',
    'cbsafp': 'CBSAFP',
    'metdivfp': 'METDIVFP',
    'funcstat': 'FUNCSTAT',
    'aland': 'ALAND',
    'awater': 'AWATER',
    'intptlat': 'INTPTLAT',
    'intptlon': 'INTPTLON',
    'geom': 'MULTIPOLYGON',
}

shp_path = '/data/tl_2020_us_county.shp'

def run(verbose=True):
    lm = LayerMapping(County, shp_path, mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


# from tiger import load_counties ; load_counties.run()
