from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import BasicAuthentication
from tastypie.constants import ALL
from trabajos.models import Trabajo


class TrabajoResource(ModelResource):
    """
    API Facet
    """

    class Meta:
        queryset = Trabajo.objects.all()
        resource_name = 'trabajo'
        allowed_methods = ['post', 'get', 'patch', 'delete']
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()
        always_return_data = True
        filtering = {"nombre": ALL}
