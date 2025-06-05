from django.urls import path, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path('', include('squad.urls')),
    path('squad/', include('squad.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
]
