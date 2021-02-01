from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Pokemons(models.Model):
  abilities = ArrayField(models.CharField(max_length=20))
  capture_rate = models.IntegerField()
  color = models.CharField(max_length=20)
  flavor_text = models.TextField()
  height = models.IntegerField()
  moves = ArrayField(models.CharField(max_length=20))
  name = models.CharField(max_length=100)
  sprites = models.JSONField()
  stats = ArrayField(models.JSONField())
  types = ArrayField(models.CharField(max_length=30))
  weight = models.IntegerField()

  class Meta: 
    verbose_name_plural = "pokemons"
  
  def __str__(self):
    return str(self.name)


class PokemonsOwn(models.Model):
  nick_name = models.CharField(max_length=20)
  is_party_menber = models.BooleanField()
  specie = models.ForeignKey(Pokemons, on_delete=models.CASCADE, default=1, verbose_name="pokemons")

  