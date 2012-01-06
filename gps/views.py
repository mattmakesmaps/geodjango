##Create your views here.
from vectorformats.Formats import Django, GeoJSON
from django.http import HttpResponse
from django.template import Context, RequestContext, loader
from django.shortcuts import render_to_response
from gps.models import GPS_Metadata, GPS_Point

# Utility Functions
def djangoToGeoJSON(request, filter_object, properties_list=None, geom_col="geom"):
    """Convert a GeoDjango QuerySet to a GeoJSON Object"""
    
    """
    Workaround for mutable default value
    TODO: Need to trap for fields not serializable
    """
    if properties_list==None:
        properties_list = filter_object[0].__dict__.keys()
    else:
        properties = []

    queryset = filter_object
    djf = Django.Django(geodjango=geom_col, properties=properties_list)
    geoj = GeoJSON.GeoJSON()
    s = geoj.encode(djf.decode(queryset))
    return s

# View Functions
def index(request):
    """Placeholder for index"""

    return render_to_response('gps/index.html', {}, context_instance=RequestContext(request))

def gps_points(request, gps_metadata_id):
    """Return GPS Points for a given Metadata ID"""

    filter_object = GPS_Point.objects.filter(gps_metadata__pk=gps_metadata_id)
    properties_list = ['name','feat_name']
    GeoJSON = djangoToGeoJSON(request, filter_object)
    return HttpResponse(GeoJSON)
