from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)


class hidrologia(models.Model):
    mslink = models.IntegerField()
    id_fenomen = models.CharField(max_length=17)
    id_tipo = models.CharField(max_length=4)
    num_hoja = models.CharField(max_length=13)
    tipo_0019 = models.CharField(max_length=3)
    tipo_0020 = models.CharField(max_length=3)
    tipo_0021 = models.CharField(max_length=3)
    tipo_0023 = models.CharField(max_length=3)
    componen1d = models.CharField(max_length=3)
    regimen = models.CharField(max_length=3)
    situacion = models.CharField(max_length=3)
    estado = models.CharField(max_length=3)
    nivel_0012 = models.CharField(max_length=3)
    nivel_0015 = models.CharField(max_length=3)
    nivel_0016 = models.CharField(max_length=3)
    nivel_0017 = models.CharField(max_length=3)
    nivel_0025 = models.CharField(max_length=3)
    canal_0012 = models.CharField(max_length=3)
    idioma = models.CharField(max_length=3)
    nombre = models.CharField(max_length=70)
    shape_leng = models.FloatField()
    geom = models.MultiLineStringField(srid=25830)

# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class CubiertaTer(models.Model):
    mslink = models.IntegerField()
    id_fenomen = models.CharField(max_length=17)
    id_tipo = models.CharField(max_length=4)
    num_hoja = models.CharField(max_length=13)
    tipo_0122 = models.CharField(max_length=3)
    tipo_0124 = models.CharField(max_length=3)
    tipo_0125 = models.CharField(max_length=3)
    tipo_0131 = models.CharField(max_length=3)
    tipo_0132 = models.CharField(max_length=3)
    tipo_0136 = models.CharField(max_length=3)
    tipo_0137 = models.CharField(max_length=3)
    componen1d = models.CharField(max_length=3)
    densidad = models.CharField(max_length=3)
    forzado = models.CharField(max_length=3)
    plant_0122 = models.CharField(max_length=3)
    riego_0123 = models.CharField(max_length=3)
    cober_0139 = models.CharField(max_length=3)
    idioma = models.CharField(max_length=3)
    nombre = models.CharField(max_length=70)
    shape_leng = models.FloatField()
    geom = models.MultiLineStringField(srid=25830)


# Auto-generated `LayerMapping` dictionary for CubiertaTer model
