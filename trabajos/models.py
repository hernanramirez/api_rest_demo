from __future__ import unicode_literals

from django.db import models


class Trabajo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
