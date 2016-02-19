"""api_rest_demo URL Configuration

"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^frontend/', include('frontend.urls')),
    url(r'^trabajos/', include('trabajos.urls')),
    url(r'^trabajos2/', include('trabajos2.urls')),
]
