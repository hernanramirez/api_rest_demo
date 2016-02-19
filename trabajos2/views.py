from trabajos.models import Trabajo
from trabajos2.serializers import TrabajoSerializer
from rest_framework import generics


class TrabajoList(generics.ListCreateAPIView):
    queryset = Trabajo.objects.all()
    serializer_class = TrabajoSerializer


class TrabajoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trabajo.objects.all()
    serializer_class = TrabajoSerializer
