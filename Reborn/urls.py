from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('squad.urls')),
    url(r'^squad/', include('squad.urls')),

    url(r'^admin/', include(admin.site.urls)),

)
