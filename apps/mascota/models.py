from django.db import models
from apps.adopcion.models import Persona

class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    #si se elimina la persona igual se eliminara la mascota
    #esto como que no me da mucho sentido :v
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna, blank=True)
    foto = models.ImageField(upload_to="mascotas/", blank=True, null=True)

    def __str__(self):
        return self.nombre
