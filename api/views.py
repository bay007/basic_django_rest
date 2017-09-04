from api import serializers
from rest_framework import viewsets
from adopcion.models import Persona
from mascota.models import Mascota, Vacuna
import django_filters

# Create your views here.


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = serializers.PersonaSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('nombre', 'edad', 'telefono', 'apellidos')


class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = serializers.MascotaSerializer


class VacunaViewSet(viewsets.ModelViewSet):
    queryset = Vacuna.objects.all()
    serializer_class = serializers.VacunaSerializer
