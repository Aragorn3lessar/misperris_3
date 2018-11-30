from django.conf.urls import url
from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('raza_lista/', views.RazaLista.as_view()),
    path('estado_lista/', views.EstadoLista.as_view()),
    path('perro_lista/', views.MascotaLista.as_view()),
    url(r'^perro_detalle/(?P<pk>[0-9]+)/$',views.MascotaDetalle.as_view()),
    url(r'^raza_detalle/(?P<pk>[0-9]+)/$',views.RazaDetalle.as_view()),
    url(r'^estado_detalle/(?P<pk>[0-9]+)/$',views.EstadoDetalle.as_view()),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)