from django.contrib import admin
from .models import Estado, Mascota, Raza, Region, Ciudad, Vivienda, TipoUser, Socio, Mascota_Adoptante
# Register your models here.
admin.site.register(Estado)
admin.site.register(Raza)
admin.site.register(Mascota)
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Vivienda)
admin.site.register(TipoUser)
admin.site.register(Socio)
admin.site.register(Mascota_Adoptante)