# Generated by Django 3.1.5 on 2021-01-30 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0005_auto_20210130_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemonsown',
            name='specie',
        ),
    ]
