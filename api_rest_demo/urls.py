"""api_rest_demo URL Configuration

"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^trabajos/', include('trabajos.urls')),
]
