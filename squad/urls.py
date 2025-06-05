from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('logo/slogo.paa', views.retlogo),
    re_path(r'^logo/(?P<user>\w{0,50})$', views.retxml),
    path('', views.overview),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
