from api import serializers
from rest_framework import viewsets
from adopcion.models import Persona

# Create your views here.


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = serializers.PersonaSerializer
