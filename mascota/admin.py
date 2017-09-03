from django.contrib import admin
from mascota.models import Mascota, Vacuna

# Register your models here.


@admin.register(Mascota, Vacuna)
class MascotaAdmin(admin.ModelAdmin):
    model = Mascota


class VacunaAdmin(admin.ModelAdmin):
    model = Vacuna
