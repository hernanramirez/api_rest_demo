from django.conf.urls import url, include
from tastypie.api import Api
from trabajos.api.resources import TrabajoResource
from django.contrib.auth.decorators import login_required

v1_api = Api(api_name='v1')
v1_api.register(TrabajoResource())

urlpatterns = [
  # ...more URLconf bits here...
  # Then add:
  url(r'^api/', include(v1_api.urls)),
]
