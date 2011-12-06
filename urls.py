from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Apps
urlpatterns = patterns('',
    url(r'^sampling/', include('sampling.urls')),
    url(r'^gps/', include('gps.urls')),
    url(r'^company/', include('company.urls')),
)

# Admin
urlpatterns += patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)
