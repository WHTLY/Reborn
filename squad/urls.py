from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^logo/(?P<user>\w{0,50})$', 'squad.views.retxml'),
    url(r'^$', 'squad.views.overview'),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)