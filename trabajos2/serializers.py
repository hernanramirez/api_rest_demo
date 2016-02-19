from rest_framework import serializers

from trabajos.models import Trabajo


class TrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajo
        fields = ('id', 'nombre', 'descripcion')
