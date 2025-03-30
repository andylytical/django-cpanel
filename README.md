# Django Development Containers

### First time run
1. `export PROJECT_NAME=djangocpanel`
1. `git clone https://github.com/andylytical/django-dev-container.git "${PROJECT_NAME}"`
1. `cd "${PROJECT_NAME}"`
1. make init
1. `sudo chown -R $USER:$USER src/"${PROJECT_NAME}"/`
1. `sed -i -e '1 i import os' src/"${PROJECT_NAME}"/settings.py`
1. Set database connection params
   1. `vim src/"${PROJECT_NAME}"/settings.py`
      ```
      DATABASES = {
         'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('POSTGRES_NAME'),
            'USER': os.environ.get('POSTGRES_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'HOST': 'db',
            'PORT': 5432,
         }
      }
      ```
1. Start the server and make sure you can connect and it provides a response
   1. `make up`
   1. http://localhost:8000
      You should see the Django development screen with a rocket.

### Develop and test locally
1. Start development server
   * `make up`
1. Edit, test, repeat.
1. Stop dev server
   * `make down`

### Clean up local dev images and containers
1. `make clean`

### References
* [Django in a container](https://github.com/docker/awesome-compose/tree/master/official-documentation-samples/django/)
* [Django Tutorial](https://docs.djangoproject.com/en/5.1/intro/tutorial01/)

# Demo project

### Create an app
As root in the web container, run the django manage.py commands
1. `make web`
1. `python manage.py startapp home`
1. `python manage.py makemigrations`
1. `python manage.py migrate`
1. (optional) `python manage.py createsuperuser`
1. `exit`

### Fill out the details for app "home"
See also: [Setup a working django project](https://ngangasn.com/deploy-django-on-shared-hosting-ultimate-guide-to-hosting-django-on-cpanel/)
1. `vim "${PROJECT_NAME}"/settings.py`
1. `vim home/urls.py`
1. `vim home/views.py`
1. `vim "${PROJECT_NAME}"/urls.py`

### References
* https://ngangasn.com/deploy-django-on-shared-hosting-ultimate-guide-to-hosting-django-on-cpanel/
* https://truehost.com/support/knowledge-base/how-to-deploy-django-web-application-on-shared-hosting-cpanel/
