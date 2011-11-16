from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geodjango.views.home', name='home'),
    # url(r'^geodjango/', include('geodjango.foo.urls')),

    # Index of the Sampling Application
    url(r'^index/$', 'sampling.views.index'),

    # Root of the client based views
    url(r'^clients/$', 'sampling.views.clients'),

    # Root of the Report based views
    url(r'^reports/$', 'sampling.views.reports'),
    url(r'^reports/(?P<report_id>\d+)/$', 'sampling.views.reports_detail'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)
