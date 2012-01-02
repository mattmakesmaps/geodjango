from django.conf.urls.defaults import patterns, include, url
from company.models import Report, Client, Project, Boundary
from sampling.models import Status

urlpatterns = patterns('company.views',
    # Index of the company application
    url(r'^$', 'index'),

    # Root of the client based views
    url(r'^clients/$', 'clients'),
    url(r'^clients/(?P<client_id>\d+)/$', 'clients_detail'),

    # Root of the Report based views
    url(r'^reports/$', 'reports'),
    url(r'^reports/(?P<report_id>\d+)/$', 'reports_detail'),

    # Root of GIS
    url(r'^geojson/$', 'geojson'),
    url(r'^geojson/boundary$', 'boundary'),
    url(r'^geojson/boundary/(?P<boundary_id>\d+)/$', 'boundary_detail'),
)
