
from django.urls import path
from . import views
from shops.views import hidrologia_view
from shops.views import MainPageView
from django.conf.urls import url
urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^hidrologia.data/', hidrologia_view, name='hidrologia'),
    url(r'^$', MainPageView.as_view()),
]
