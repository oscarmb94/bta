import os
from django.contrib.gis.utils import LayerMapping
from .models import shops
cubiertater_mapping = {
    'mslink': 'mslink',
    'id_fenomen': 'id_fenomen',
    'id_tipo': 'id_tipo',
    'num_hoja': 'num_hoja',
    'tipo_0122': 'TIPO_0122',
    'tipo_0124': 'TIPO_0124',
    'tipo_0125': 'TIPO_0125',
    'tipo_0131': 'TIPO_0131',
    'tipo_0132': 'TIPO_0132',
    'tipo_0136': 'TIPO_0136',
    'tipo_0137': 'TIPO_0137',
    'componen1d': 'COMPONEN1D',
    'densidad': 'DENSIDAD',
    'forzado': 'FORZADO',
    'plant_0122': 'PLANT_0122',
    'riego_0123': 'RIEGO_0123',
    'cober_0139': 'COBER_0139',
    'idioma': 'IDIOMA',
    'nombre': 'NOMBRE',
    'shape_leng': 'Shape_Leng',
    'geom': 'MULTILINESTRING25D',
}

cubiertater_shp = os.path.abspath(os.path.join('btashp', 'BTA-AB_2006_01_E10_742-3-4_CubiertaTer_lin_BTAv1_25830.shp'))

def run(verbose=True):
    lm = LayerMapping(shops, cubiertater_shp, cubiertater_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)
