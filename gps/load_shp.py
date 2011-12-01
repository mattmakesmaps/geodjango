# From https://docs.djangoproject.com/en/dev/ref/contrib/gis/tutorial/#layermapping

import os
from django.contrib.gis.utils import LayerMapping
from gps.models import GPS_Point, Feature_Type

field_mapping = {
    'name': 'Comment',
    'max_pdop': 'Max_PDOP',
    'gps_date': 'GPS_Date',
    'gps_time': 'GPS_Time',
    'feat_name': 'Feat_Name',
    'feature_type' : {'name':'Category'},
    'geom': 'MultiPoint',
}

ds = os.path.abspath('/home/matt/Dropbox/Junk/Export/237T2Dump/Point_ge.shp')

def run(verbose=True):
    lm = LayerMapping(GPS_Point, ds, field_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
