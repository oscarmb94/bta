from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop, CubiertaTer,hidrologia


from mapwidgets.widgets import GooglePointFieldWidget

admin.site.site_header='Actualización de base de datos'
# Register your models here.



@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
    default_lon = 1400000
    default_lat = 7495000
    default_zoom = 12


@admin.register(hidrologia)
class hidrologiaAdmin(OSMGeoAdmin):
    list_display = ('id', 'geom')
    default_lon = 1400000
    default_lat = 7495000
    default_zoom = 12



@admin.register(CubiertaTer)
class CubiertaTerAdmin(OSMGeoAdmin):
    list_display = ('nombre', 'num_hoja')
    default_lon = 1400000
    default_lat = 7495000
    default_zoom = 12



#class ShopAdmin(admin.ModelAdmin):
#    formfield_overrides = {
#        models.PointField: {"widget": GooglePointFieldWidget}
#    }
