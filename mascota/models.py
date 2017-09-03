from django.db import models
from adopcion.models import Persona
# Create your models here.


class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'vacuna'

    def __str__(self):
        return self.nombre


class Mascota(models.Model):

    folio = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_rescate = models.DateTimeField()

    vacuna = models.ManyToManyField(
        Vacuna, related_name='inocuacion', db_table='inocuacion')
    persona = models.ForeignKey(
        Persona, null=True, related_name='duenio', on_delete=models.CASCADE)

    class Meta:
        db_table = 'mascota'

    def __str__(self):
        return self.nombre
