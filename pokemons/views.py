from rest_framework import viewsets, permissions
from . import models
from . import serializers
from rest_framework.response import Response

class PokemonsViewset(viewsets.ModelViewSet):
  queryset = models.Pokemons.objects.all()
  serializer_class = serializers.PokemonsSerializer

class PokemonsOwnViewset(viewsets.ModelViewSet):
  queryset = models.PokemonsOwn.objects.all()
  serializer_class = serializers.PokemonsOwnSerializer
