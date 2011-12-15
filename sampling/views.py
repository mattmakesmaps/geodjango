#Create your views here.
from vectorformats.Formats import Django, GeoJSON
from company.models import Report, Client, Project, Boundary
from sampling.models import Status
from django.http import HttpResponse
from django.template import Context, RequestContext, loader
from django.shortcuts import render_to_response

# Uses render_to_response()
# NOTE: render_to_response() requires third argument to override default context.
# This is required to access STATIC_URL variable in template
def reports_detail(request, report_id):
    report_detail = Report.objects.get(pk=report_id)
    report_status = Status.objects.filter(report__pk=report_id)[0]
  
    # Slog through the models and get a boundary from a report
    # TODO Try walking all the way up in one call
    project = Project.objects.get(report__pk=report_id)
    client = Client.objects.get(project__pk=project.id)
    boundary = Boundary.objects.get(client=client.id)

    return render_to_response('sampling/reports_detail.html', {'report_detail': report_detail, 'report_status':report_status, 'boundary': boundary}, context_instance=RequestContext(request))
