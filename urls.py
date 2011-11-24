from django.conf.urls.defaults import patterns, include, url
from sampling.models import Report, Client, Project, Status, Boundary

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('sampling.views',
    # Index of the sampling application
    url(r'^index/$', 'index'),

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

urlpatterns += patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)
