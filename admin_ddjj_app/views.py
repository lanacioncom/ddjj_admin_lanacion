from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from models import TipoBien

def tipo_bien(request):
    data = serializers.serialize("json", TipoBien.objects.all())
    return HttpResponse(data)
