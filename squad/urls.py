from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = patterns('',
    url(r'^logo/(?P<user>\w{0,50})$', 'squad.views.retxml'),
    url(r'^logo/slogo\.paa$', 'squad.views.retlogo'),
    url(r'^$', 'squad.views.overview'),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)