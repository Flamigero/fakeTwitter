# FakeTwitter

Simple faketwitter project

## Starting ๐

```
git clone https://github.com/Flamigero/fakeTwitter.git
```

### Pre-requirements ๐

To run the project we need:
Docker and docker compose


### Instalation ๐ง

To execute and install the app we have to do:

Run docker compose

```
docker-compose -f local.yml build
```

```
docker-compose -f local.yml run
```

When the process finished we can go to localhost:8000
You can change the port in the file init.sh

## Tests โ๏ธ

To run the app's tests you have to run this docker command:

```
docker-compose -f local.yml run django python manage.py test
```

## Build with ๐ ๏ธ

This are the tools I have used

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Docker and Docker-Compose](https://www.docker.com/)

## Author โ๏ธ

* **Carlos Nรบรฑez** - *Developer* - [Flamigero](https://github.com/Flamigero)