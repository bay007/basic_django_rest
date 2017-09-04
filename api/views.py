from api import serializers
from rest_framework import viewsets
from adopcion.models import Persona
from mascota.models import Mascota, Vacuna

# Create your views here.


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = serializers.PersonaSerializer


class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = serializers.MascotaSerializer


class VacunaViewSet(viewsets.ModelViewSet):
    queryset = Vacuna.objects.all()
    serializer_class = serializers.VacunaSerializer
