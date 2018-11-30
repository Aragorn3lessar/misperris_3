from django.shortcuts import render
from .models import Raza, Mascota, Estado
from .serializers import RazaSerializer, MascotaSerializer, EstadoSerializer
from rest_framework import generics
# Create your views here.


class RazaLista(generics.ListCreateAPIView):
    queryset = Raza.objects.all()
    serializer_class = RazaSerializer

class EstadoLista(generics.ListCreateAPIView):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class MascotaLista(generics.ListCreateAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer


class RazaDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Raza.objects.all()
    serializer_class = RazaSerializer

class EstadoDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class MascotaDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    