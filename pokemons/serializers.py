from rest_framework import serializers
from . import models


class PokemonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pokemons
        fields = (
            "id",
            "abilities",
            "capture_rate",
            "color",
            "flavor_text",
            "height",
            "moves",
            "name",
            "sprites",
            "stats",
            "types",
            "weight",
        )

class PokemonsOwnSerializer(serializers.ModelSerializer):
    class Meta:
        model = (models.PokemonsOwn, models.Pokemons)
        fields = (
            "id",
            "nick_name",
            "is_party_menber",
            "specie", 
        )
