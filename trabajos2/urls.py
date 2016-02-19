from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from trabajos2.views import TrabajoList, TrabajoDetail

urlpatterns = [
    url(r'^trabajos$', TrabajoList.as_view()),
    url(r'^trabajos/(?P<pk>[0-9]+)/$', TrabajoDetail.as_view()),
]
