from django.test import TestCase

# Create your tests here.
from .models import Mascota, Estado, Raza, Socio

class SocioTestCase(TestCase):
   def setUp(self):
    a1 = Mascota.objects.create(name="1", foto="default", nombre="JK", raza="Pequines", descripcion="se llama JK", estado="adoptado")
    a2 = Mascota.objects.create(name="2", foto="default", nombre="Queque", raza="Labrador", descripcion="se llama Queque", estado="disponible")
    s1 = Socio.objects.create(name="11883419-4", correo="bb@gmail.com", nombre="Iván", fecha_n="1999-01-01", telefono="12345678", region="Santiago", ciudad="Puente Alto", tipo_viv="Departamento", contrasena="1234", tipo_user="admin")
    s2 = Socio.objects.create(name="12345678-9", correo="lolo@gmail.com", nombre="Freddy", fecha_n="1973-09-11", telefono="12345678", region="Santiago", ciudad="Puente Alto", tipo_viv="Casa con patio grande", contrasena="1234", tipo_user="socio")
    Socio.objects.create(s1)
    Mascota.objects.create(a1)
    Socio.objects.create(s2)
    Mascota.objects.create(a2)