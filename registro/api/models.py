from django.db import models

# Create your models here.

# Create your models here.
class Estado(models.Model):
    name=models.CharField(max_length=45,default='')

    def __str__(self):
        return self.name

class Raza(models.Model):
    name=models.CharField(max_length=45,default='')

    def __str__(self):
        return self.name

class Mascota(models.Model):
    name=models.CharField(max_length=45,default='')
    foto = models.ImageField(upload_to='media',verbose_name=u'Imágen')
    nombre=models.CharField(max_length=45)
    raza=models.ForeignKey(Raza,on_delete=models.CASCADE)
    descripcion=models.TextField()
    estado=models.ForeignKey(Estado,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
