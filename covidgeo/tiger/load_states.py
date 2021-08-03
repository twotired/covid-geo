from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import State

mapping = {
    'region': 'REGION',
    'division': 'DIVISION',
    'statefp': 'STATEFP',
    'statens': 'STATENS',
    'geoid': 'GEOID',
    'stusps': 'STUSPS',
    'name': 'NAME',
    'lsad': 'LSAD',
    'mtfcc': 'MTFCC',
    'funcstat': 'FUNCSTAT',
    'aland': 'ALAND',
    'awater': 'AWATER',
    'intptlat': 'INTPTLAT',
    'intptlon': 'INTPTLON',
    'geom': 'MULTIPOLYGON',
}

shp_path = '/data/tl_2020_us_state.shp'

def run(verbose=True):
    lm = LayerMapping(State, shp_path, mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


# from tiger import load_states ; load_states.run()
