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


## API Docs
[API.md](./API.md)


## Discussion
I developed this api and corresponding [client](https://github.com/bbonsign/aq_client) separately, so that each could be run without the other.

With projects like this, I usually try to use a tool that I haven't used much before, in this case the Django Rest Framework (DRF)
since I already have some experience using Django.
A benefit of using DRF is that it provides a lot of good default functionality (e.g. the [api root](http://localhost:8000/api/v1/) provides
hyperlinks to the parameters and cities endpoints).  On the other hand, ...

