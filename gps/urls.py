from django.conf.urls.defaults import patterns, include, url
from gps.models import *

urlpatterns = patterns('gps.views',
    # Index of the sampling application
    url(r'^index/$', 'index'),

)
