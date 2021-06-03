# FakeTwitter

Simple faketwitter project

## Starting 🚀

```
git clone https://github.com/Flamigero/fakeTwitter.git
```

### Pre-requirements 📋

To run the project we need:
Docker and docker compose


### Instalation 🔧

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

## Tests ⚙️

To run the app's tests you have to run this docker command:

```
docker-compose -f local.yml run django python manage.py test
```

## Build with 🛠️

This are the tools I have used

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Docker and Docker-Compose](https://www.docker.com/)

## Author ✒️

* **Carlos Núñez** - *Developer* - [Flamigero](https://github.com/Flamigero)