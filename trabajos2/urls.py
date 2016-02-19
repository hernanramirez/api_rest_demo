from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from trabajos2.views import TrabajoList, TrabajoDetail

urlpatterns = [
    url(r'^trabajo$', TrabajoList.as_view()),
    url(r'^trabajo/(?P<pk>[0-9]+)/$', TrabajoDetail.as_view()),
]
