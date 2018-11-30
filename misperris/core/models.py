from django.db import models

# Create your models here.
class Estado(models.Model):
    name=models.CharField(max_length=45,primary_key=True)

    def __str__(self):
        return self.name

class Raza(models.Model):
    name=models.CharField(max_length=45,primary_key=True)

    def __str__(self):
        return self.name

class Region(models.Model):
    name=models.CharField(max_length=45,primary_key=True)

    def __str__(self):
        return self.name

class Ciudad(models.Model):
    name=models.CharField(max_length=45,primary_key=True)
    region=models.ForeignKey(Region,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Vivienda(models.Model):
    name=models.CharField(max_length=45,primary_key=True)

    def __str__(self):
        return self.name

class TipoUser(models.Model):
    name=models.CharField(max_length=45,primary_key=True)

    def __str__(self):
        return self.name


class Socio(models.Model):
    name=models.CharField(max_length=45,primary_key=True)
    correo=models.CharField(max_length=100)
    nombre=models.CharField(max_length=245)
    fecha_n=models.DateField()
    telefono=models.IntegerField()
    region=models.ForeignKey(Region,on_delete=models.CASCADE)
    ciudad=models.ForeignKey(Ciudad,on_delete=models.CASCADE)
    tipo_viv=models.ForeignKey(Vivienda,on_delete=models.CASCADE)
    contrasena=models.CharField(max_length=100)
    tipo_user=models.ForeignKey(TipoUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


class Mascota(models.Model):
    name=models.CharField(max_length=45,primary_key=True)
    foto = models.ImageField(upload_to='media',verbose_name=u'Imágen')
    nombre=models.CharField(max_length=45)
    raza=models.ForeignKey(Raza,on_delete=models.CASCADE)
    descripcion=models.TextField()
    estado=models.ForeignKey(Estado,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Mascota_Adoptante(models.Model):
    id_socio=models.ForeignKey(Socio,on_delete=models.CASCADE)
    id_mascota=models.ForeignKey(Mascota,on_delete=models.CASCADE,  primary_key=True)
