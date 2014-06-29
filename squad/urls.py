from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',

    url(r'^$', 'squad.views.overview'),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)