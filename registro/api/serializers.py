from rest_framework import serializers
from .models import Raza, Estado, Mascota

class RazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raza
        fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ('name', 'foto', 'nombre', 'raza', 'descripcion', 'estado')
