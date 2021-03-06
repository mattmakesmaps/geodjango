# From https://docs.djangoproject.com/en/dev/ref/contrib/gis/tutorial/#layermapping

import os
from django.contrib.gis.utils import LayerMapping
from company.models import Boundary

field_mapping = {
    'name': 'NAME10',
    'name_formal': 'NAMELSAD10',
    'geom': 'MULTIPOLYGON'
}

shp = os.path.abspath('/home/matt/Downloads/WA_Tribal/tl_2010_53_aiannh10.shp')

def run(verbose=True):
    lm = LayerMapping(Boundary, shp, field_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
