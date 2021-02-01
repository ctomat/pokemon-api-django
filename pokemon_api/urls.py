"""pokemon_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers
from login import views
from pokemons import views as pokemons_views

router = routers.DefaultRouter()
router.register(r'api/v1/login', views.UserViewSet)
router.register(r'api/v1/groups', views.GroupViewSet)
router.register(r'pokemons', pokemons_views.PokemonsViewset)
router.register(r'pokemonown', pokemons_views.PokemonsOwnViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
