# Company View Functions
from vectorformats.Formats import Django, GeoJSON
from company.models import Report, Client, Project, Boundary
from sampling.models import Status
from django.http import HttpResponse
from django.template import Context, RequestContext, loader
from django.shortcuts import render_to_response

# Uses render_to_response()
def index(request):
    report_list = Report.objects.all()
    return render_to_response('company/index.html', {'report_list': report_list}, context_instance=RequestContext(request))

# Uses render_to_response()
def clients(request):
    client_list = Client.objects.all()
    project_list = Project.objects.order_by('-name')
    return render_to_response('company/clients.html', {'client_list': client_list, 'project_list': project_list}, context_instance=RequestContext(request))

# For a given client, grab associated projects
# __TODO__ grab reports associated with a project
def clients_detail(request, client_id):
    project_list = Project.objects.filter(client__pk=client_id)
    return render_to_response('company/clients_detail.html', {'project_list': project_list}, context_instance=RequestContext(request))

# Uses render_to_response()
def reports(request):
    report_list = Report.objects.all()
    return render_to_response('company/reports.html', {'report_list': report_list}, context_instance=RequestContext(request))

# Uses render_to_response()
# NOTE: render_to_response() requires third argument to override default context.
# This is required to access STATIC_URL variable in template
def reports_detail(request, report_id):
    report_detail = Report.objects.get(pk=report_id)
    report_status = Status.objects.filter(report__pk=report_id)[0]

    # Attempt to reduce the number of database calls using 
    # select_related() to traverse the joins.
   # project = Project.objects.select_related().get(report__pk=report_id)

    # Slog through the models and get a boundary from a report
    # TODO Try walking all the way up in one call
    project = Project.objects.get(report__pk=report_id)
    client = Client.objects.get(project__pk=project.id)
    boundary = Boundary.objects.get(client=client.id)
    
    return render_to_response('sampling/reports_detail.html', {'report_detail': report_detail, 'report_status':report_status, 'boundary': boundary}, context_instance=RequestContext(request))

# Using CRSchmidt's vectorfeatures module, create a real
# GeoJSON FeatureCollection.
def boundary_detail(request, boundary_id):
    boundary_detail = Boundary.objects.filter(pk=boundary_id)
    djf = Django.Django(geodjango="geom", properties=['name','name_formal'])
    geoj = GeoJSON.GeoJSON()
    s = geoj.encode(djf.decode(boundary_detail))
    return HttpResponse(s)

def boundary(request):
    return HttpResponse("Move Along... Move Along")

def geojson(request):
    return HttpResponse("Move Along... Move Along")
