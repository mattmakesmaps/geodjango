##Create your views here.
from django.http import HttpResponse
from django.template import Context, RequestContext, loader
from django.shortcuts import render_to_response
from gps.models import GPS_Metadata, GPS_Point
        
# Project Shortcuts
from geodjango.shortcuts import djangoToGeoJSON

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
