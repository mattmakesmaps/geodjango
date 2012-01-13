##Create your views here.
from vectorformats.Formats import Django, GeoJSON
from django.http import HttpResponse
from django.template import Context, RequestContext, loader
from django.shortcuts import render_to_response
from gps.models import GPS_Metadata, GPS_Point
from decimal import Decimal
from datetime import date
import django.db.models.base

# Utility Functions
def djangoToGeoJSON(request, filter_object, properties_list=None, geom_col="geom"):
    """Convert a GeoDjango QuerySet to a GeoJSON Object"""
    
    #Workaround for mutable default value
    if properties_list==None:
        properties_list = []
        #Return dictionary of key value pairs
        filter_dict = filter_object[0].__dict__
        #Remove bunk fields
        for d in filter_dict:
            if isinstance(filter_dict[d], django.db.models.base.ModelState):
                pass
            elif isinstance(filter_dict[d], Decimal):
                #Either handle or change to float
                for obj in filter_object:
                    setattr(obj, d, float(obj.__dict__[d]))
                properties_list.append(d)    
            # Convert date to string
            elif isinstance(filter_dict[d], date):
                for obj in filter_object:
                    setattr(obj, d, str(obj.__dict__[d]))
                properties_list.append(d)
            else:
                properties_list.append(d)

        properties_list.remove(geom_col)
    else:
        properties_list = []

    queryset = filter_object
    djf = Django.Django(geodjango=geom_col, properties=properties_list)
    decode_djf = djf.decode(queryset)
    """
    TODO: Decode into vectorfeatures objects. Check for type, then address
          before encode to GeoJSON. str() date, maybe same for decimal?
    """
    geoj = GeoJSON.GeoJSON()
    s = geoj.encode(decode_djf)
    return s

# View Functions
def index(request):
    """Placeholder for index"""

    return render_to_response('gps/index.html', {}, context_instance=RequestContext(request))

def gps_points(request, gps_metadata_id):
    """Return GPS Points for a given Metadata ID"""

    filter_object = GPS_Point.objects.filter(gps_metadata__pk=gps_metadata_id)
    #properties_list = ['name','feat_name']
    GeoJSON = djangoToGeoJSON(request, filter_object)
    return HttpResponse(GeoJSON)
