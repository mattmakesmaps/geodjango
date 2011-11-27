##Create your views here.
from vectorformats.Formats import Django, GeoJSON
from django.http import HttpResponse
from django.template import Context, RequestContext, loader
from django.shortcuts import render_to_response

# Uses render_to_response()
def index(request):
    return render_to_response('gps/index.html', {}, context_instance=RequestContext(request))

