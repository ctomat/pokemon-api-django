# Pokemon API in django

## Deploy in a local environment.

  1. Create a dir where all the project files will be stored and clone de repository
```sh
mkdir pokemon
cd pokemon
git clone https://github.com/ctomat/pokemon-api-django.git
```
  2. Create a virtual environment to isolate our package dependencies locally
```sh
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
  3. Install required packages from requirements.txt
```sh
pip install -r requirements.txt --no-index --find-links file:///tmp/packages
``` 
  4. Connect the API with your database en `pokemon_api/settings.py`
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database-name',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
``` 
   5. Now sync your database for the first time
```sh
python manage.py makemigrations
python manage.py migrate
```
   6. Create a initial user
```sh
python manage.py createsuperuser --email admin@example.com --username admin
```
   7. Run the server
```sh
python manage.py runserver
```

## Paths
```python
router.register(r'api/v1/login', views.UserViewSet)
router.register(r'api/v1/groups', views.GroupViewSet)
router.register(r'pokemons', pokemons_views.PokemonsViewset)
router.register(r'pokemonown', pokemons_views.PokemonsOwnViewset)
``` 
