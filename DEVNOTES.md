````shell
mkdir storefront
cd storefront
pipenv install django
# Creates Pipfile and Pipfile.lock
pip install pipenv
pipenv shell

# CREATE A VIRTUAL ENVIRONMENT
# cd into project storefront
# python3 --version
```shell
pipenv --python 3.11.3
````

```shell
# Checks for Django install
django-admin

# create storefront in root folder with dot (.)
django-admin startproject storefront .

# Error regarding configuration
django-admin runserver

#Server runs on port 8000
python manage.py runserver
```

# Django Debug Toolbar Installation Instructions

[Django Debug Toolbar Installation Process](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)

1. Python vs Virtual ENV:

```shell
$ python -m pip install django-debug-toolbar
# vs
$ pipenv install django-debug-toolbar
```

2. Settings module add app

```python
# storefront/settings.py
INSTALLED_APPS = [
...
    'playground',
    'debug_toolbar',
]
```

3. Setting up URLconf

```python
# storefront/urls.py
import debug_toolbar

urlpatterns = [
  ...
  path('__debug__/', include(debug_toolbar.urls))
]
```

4. Add the Middleware

```python
# storefront/settings.py
MIDDLEWARE = [
  'debug_toolbar.middleware.DebugToolbarMiddleware',
]
```

5. Configure Internal IPs

```python
# storefront/settings.py
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
```

### JIRA Ticket

App: likes
LikedItem

- what user likes what object
- user: ForeignKey to User (django.contrib.auth.models)

### JIRA Ticket

- Add zip code to Address
- Create a migration
- Run it
- Inspect the migrations table

[MySQL Community Server Download](https://dev.mysql.com/downloads/mysql/)

[DataGrip by Jet Brains](https://www.jetbrains.com/datagrip/download/#section=mac)

[Generating Dummy Data](https://mockaroo.com/)
