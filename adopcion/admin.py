from django.contrib import admin
from adopcion.models import Persona

# Register your models here.


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    description = "Clientes deños de mascotas"
    model = Persona
    empty_value_display = '-Ninguno-'
