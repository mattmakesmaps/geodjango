#Create your views here.
from vectorformats.Formats import Django, GeoJSON
from sampling.models import Report, Client, Project, Status, ResBnd
from django.http import HttpResponse
from django.template import Context, RequestContext, loader
from django.shortcuts import render_to_response

# Uses render_to_response()
def index(request):
    report_list = Report.objects.all()
    return render_to_response('sampling/index.html', {'report_list': report_list}, context_instance=RequestContext(request))

# Uses render_to_response()
def clients(request):
    client_list = Client.objects.all()
    project_list = Project.objects.order_by('-name')
    return render_to_response('sampling/clients.html', {'client_list': client_list, 'project_list': project_list}, context_instance=RequestContext(request))

# For a given client, grab associated projects
# __TODO__ grab reports associated with a project
def clients_detail(request, client_id):
    project_list = Project.objects.filter(client__pk=client_id)
    return render_to_response('sampling/clients_detail.html', {'project_list': project_list})

# Uses render_to_response()
def reports(request):
    report_list = Report.objects.all()
    return render_to_response('sampling/reports.html', {'report_list': report_list}, context_instance=RequestContext(request))

# Uses render_to_response()
# NOTE: render_to_response() requires third argument to override default context.
# This is required to access STATIC_URL variable in template
def reports_detail(request, report_id):
    report_detail = Report.objects.get(pk=report_id)
    report_status = Status.objects.filter(report__pk=report_id)[0]
    return render_to_response('sampling/reports_detail.html', {'report_detail': report_detail, 'report_status':report_status}, context_instance=RequestContext(request))

# Using CRSchmidt's vectorfeatures module, create a real
# GeoJSON FeatureCollection.
def resbnd_detail(request, resbnd_id):
    resbnd_detail = ResBnd.objects.filter(pk=resbnd_id)
    djf = Django.Django(geodjango="mpoly", properties=['name','name_formal'])
    geoj = GeoJSON.GeoJSON()
    s = geoj.encode(djf.decode(resbnd_detail))
    return HttpResponse(s)
