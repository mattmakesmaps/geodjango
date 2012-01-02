##Create your views here.
from vectorformats.Formats import Django, GeoJSON
from django.http import HttpResponse
from django.template import Context, RequestContext, loader
from django.shortcuts import render_to_response
from gps.models import GPS_Metadata, GPS_Point

# Uses render_to_response()
def index(request):
    return render_to_response('gps/index.html', {}, context_instance=RequestContext(request))

"""
Return GPS Points for a given event.
TODO: Maybe turn into a factory function accepting
      different geometry types.
"""
def gps_points(request, gps_metadata_id):
    gps_data = GPS_Point.objects.filter(gps_metadata__pk=gps_metadata_id)
    djf = Django.Django(geodjango="geom", properties=['name','feat_name'])
    geoj = GeoJSON.GeoJSON()
    s = geoj.encode(djf.decode(gps_data))
    return HttpResponse(s)
