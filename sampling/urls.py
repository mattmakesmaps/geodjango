from django.conf.urls.defaults import patterns, include, url
from company.models import Report, Client, Project, Boundary
from sampling.models import Status

urlpatterns = patterns('sampling.views',
    url(r'^reports/(?P<report_id>\d+)/$', 'reports_detail'),
)
