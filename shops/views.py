from django.shortcuts import render
from .models import Shop
from .models import hidrologia
from django.http import HttpResponse
from django.core.serializers import serialize
from django.views.generic import TemplateView #viw para html
# Create your views here.

#view muestra datos json renderizados
def hidrologia_view(request):
    hidrologia_as_geojson = serialize('geojson', hidrologia.objects.all())
    return HttpResponse(hidrologia_as_geojson, content_type='json')



#view html
class MainPageView(TemplateView):
    template_name = 'bta/index.html'
