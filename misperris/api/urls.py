from django.urls import path
from .views import listar_mascota, agregar_mascota, eliminar_mascota,modificar_mascota

urlpatterns = [
    path('listar-mascota/', listar_mascota, name="api_listar_mascota"),
    path('agregar-mascota/', agregar_mascota, name="api_agregar_mascota"),
    path('eliminar-mascota/<id>/', eliminar_mascota, name="api_eliminar_mascota"),
    path('modificar-mascota/', modificar_mascota, name="api_modificar_mascota"),
]

