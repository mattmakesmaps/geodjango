# From https://docs.djangoproject.com/en/dev/ref/contrib/gis/tutorial/#layermapping

import os
from django.contrib.gis.utils import LayerMapping
from models import ResBnd

field_mapping = {
    'name': 'NAME10',
    'name_formal': 'NAMELSAD10',
    'mpoly': 'MULTIPOLYGON'
}

shp = os.path.abspath('/home/matt/Downloads/ak_tribal/tl_2010_02_aiannh10.shp')

def run(verbose=True):
    lm = LayerMapping(ResBnd, shp, field_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
