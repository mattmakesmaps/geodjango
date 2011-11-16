#Create your views here.
from sampling.models import Report, Client, Project, Status
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response

"""
# Hardcoded
def index(request):
    latest_report_list = Report.objects.all()[:5]
    output = ', '.join(r.name for r in latest_report_list)
    return HttpResponse(output)
"""

"""
# Uses template
def index(request):
    # get all reports
    report_list = Report.objects.all()

    t = loader.get_template('sampling/index.html')

    # The context is a dictionary mapping
    # template variable names to Python objects
    c = Context({
        'report_list': report_list,
    })

    return HttpResponse(t.render(c))
"""

# Uses render_to_response()
def index(request):
    report_list = Report.objects.all()
    return render_to_response('sampling/index.html', {'report_list': report_list})

# Uses render_to_response()
def clients(request):
    client_list = Client.objects.all()
    project_list = Project.objects.all()
    return render_to_response('sampling/clients.html', {'client_list': client_list, 'project_list': project_list})

# Uses render_to_response()
def reports(request):
    report_list = Report.objects.all()
    return render_to_response('sampling/index.html', {'report_list': report_list})

def reports_detail(request):
    report_list = Report.objects.all()
    status_list = Status.objects.all()
    return render_to_response('sampling/reports_detail.html', {'report_list': report_list, 'status_list': status_list})
