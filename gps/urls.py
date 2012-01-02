from django.conf.urls.defaults import patterns, include, url
from gps.models import GPS_Point, GPS_Metadata

urlpatterns = patterns('gps.views',
    # Index of the sampling application
    url(r'^index/$', 'index'),
    url(r'^geojson/points/(?P<gps_metadata_id>\d+)/$', 'gps_points'),
)
