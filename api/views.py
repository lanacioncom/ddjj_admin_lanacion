from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from serializers import PersonaSerializer, PersonaDDJJSerializer, DDJJBienSerializer
from admin_ddjj_app.models import Persona, Ddjj

from django.views.decorators.cache import cache_page
class PersonaViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Persona.objects.exclude(personacargo = None)
        serializer = PersonaSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Persona.objects.exclude(personacargo = None)
        persona = get_object_or_404(queryset, pk=pk)
        serializer = PersonaDDJJSerializer(persona)
        return Response(serializer.data)

class DDJJBienViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Ddjj.objects.exclude(status = 0)
        ddjj = get_object_or_404(queryset, pk=pk)
        serializer = DDJJBienSerializer(ddjj.bienes, many = True)
        return Response(serializer.data)

