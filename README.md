# OpenAQ API


## Description
A REST Api made with Django + Django Rest Framework


## Set up
Change into project directory (containing this README).
If you have `pipenv` installed:
```shell
pipenv install
```
and then to enter the Python virtual environment:
```
pipenv shell
```
Without `pipenv`, create a virtual environment and use [requirements.txt](./requirements.txt) to install the dependencies.

Once the dependencies are installed, we need to set up the environment and database:
```
cp config/.env.sample config/.env
python manage.py migrate
python manage.py seed_measuremnts
```
The last command adds some sample data to the SQLite database specified in [config/.env](./config/.env).

Finally, start the server with
```
python manage.py runserver
```
which will be listening on port 8000.  You can kill the server with Ctrl-C

If you want to interact with the Django admin page, create a superuser `python manage.py createsuperuser` and then restart
the server and navigate to <http://localhost:8000/admin/>

### Notable Files
For those unfamiliar with the structure of Django project, the main settings are in [config/settings.py](.config/settings.py) and the majority
of the custom code is in app-specific directories.  In this case there is one app named `api`, in which [models.py](./api/models.py) sets up the models
used for structuring the database.  For the DRF, [api/serializers.py](./api/serializers.py) and [api/views.py](./api/views.py) contain the function
for the endpoints.  The routes are registered in the project-wide [config/urls.py](./config/urls.py) and app-specific [api/urls.py](./api/urls.py).


## API Docs
[API.md](./API.md)


## Discussion
I developed this api and corresponding [client](https://github.com/bbonsign/aq_client) separately, so that each could be run without the other.
I was hoping to mimic a subset OpenAQ Api endpoints, limited to the United States and with fewer optional query parameters.

With projects like this, I usually try to use a tool that I haven't used much before, in this case the Django Rest Framework (DRF)
since I already have some experience using Django.
A benefit of using DRF is that it provides a lot of good default functionality (e.g. the [api root](http://localhost:8000/api/v1/) provides
hyperlinks to the parameters and cities endpoints).  On the other hand, the DRF is extensive and I found it difficult to identify how to override
the default behavior in some cases.  For example, using the class-based views for the measurements endpoint worked well for listing measurements and
providing filtering via a query string, but I couldn't figure out how to change the default `?location_city_name=` parameter to just `?city=`.
Similarly, I could get the POST method at `api/v1/measurements/` to work, so I made a `api/v1/measurements/add` endpoint for adding new measurements,
breaking the standard pattern for REST APIs.  Another inconsistency, is that the [api root](http://localhost:8000/api/v1/) provides links for the
parameters and cities endpoints, but not the locations and measurements endpoints that are also available.

In retrospect, it might have been better to write function-based views (instead of the class-based views provided by Django/DRF) for each endpoint/Http method,
similar to how setting up a basic Api with Flask or Express.js would go.  This alternative would have smoothed some of the rough edges I see in
my Api so far, at the expense of writing more boiler plate code.

Performance is another issue that arose with DRF.  With nested relationships between my models, e.g. measurements having a foreign key to locations, the amount
of redundant database queries generated in the background can skyrocket, causing a very slow response from the server.  I was able to alleviate this after
some research via the `setup_eager_loading` and `get_queryset` methods in [api/serializers.py](./api/serializers.py) and [api/views.py](./api/views.py).
