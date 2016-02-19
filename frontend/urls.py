from django.conf.urls import url
from frontend.views import FrontendView

urlpatterns = [
  # ...more URLconf bits here...
  # Then add:
  url(r'^view/$', FrontendView.as_view(), name='frontend'),
]
