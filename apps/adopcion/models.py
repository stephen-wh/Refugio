from django.db import models

# Create your models here.
#from apps.adopcion.models import Persona
 

# class Vacuna(models.Model):
#     mombre = models.CharField(max_length=50)

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono= models.CharField( null=True, max_length=12)
    email = models.EmailField()
    domicilio = models.TextField()

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellidos)

class Solicitud(models.Model):
    persona = models.ForeignKey(Persona, null=True, blank=True)
    numero_mascotas = models.IntegerField()
    razones = models.TextField() 
