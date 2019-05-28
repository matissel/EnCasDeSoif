[![Build Status](https://travis-ci.com/Matissou/EnCasDeSoif.svg?branch=master)](https://travis-ci.com/Matissou/EnCasDeSoif) [![codecov](https://codecov.io/gh/Matissou/EnCasDeSoif/branch/master/graph/badge.svg)](https://codecov.io/gh/Matissou/EnCasDeSoif) [![docker badge](https://images.microbadger.com/badges/image/loicrosso/en-cas-de-soif.svg)](https://microbadger.com/images/loicrosso/en-cas-de-soif)
# EnCasDeSoif
![Logo EnCasDeSoif](https://raw.githubusercontent.com/Matissou/EnCasDeSoif/master/EnCasDeSoif/static/img/logo_ecds.png)


Bienvenue sur **En cas de soif**. Cette application web permet de trouver les points d'eaux les plus proches.
Que ce soit pour boire, mettre de l'eau sur un bobo ou même se laver, cette application communautaire saura répondre à vos attentes !

## Installation 

### Avec docker
#### Prérequis
- Docker

```bash
$ docker pull loicrosso/en-cas-de-soif
$ docker run --rm --name EnCasDeSoif -p 8000:8000 \
                -e MAPBOX_LOGIN="MyMapboxUsername" \
                -e MAPBOX_PRIVATE_KEY="sk.MyMapBoxSecretKey" \
                loicrosso/en-cas-de-soif
```
> Go to localhost:8000

### Depuis les sources
#### Prérequis
- Python 3.7
- Pip

```bash
$ git clone https://github.com/Matissou/EnCasDeSoif
$ cd EnCasDeSoif
# Modifiez le fichier .env avec votre login et clé d'api Mapbox 
# Sourcez le fichier .env
$ source .env
#installer les dépendances
$ pip install -r requirements.txt
# préparer la base de données
$ python manage.py makemigrations && python manage.py migrate
# lancer le serveur
$ python manage.py runserver
```

> Go to localhost:8000


[//]: <> (Pour générer le tableau à partir du CSV : https://www.tablesgenerator.com/markdown_tables)
### API
Il est possible d'utiliser EnCasDeSoif en utilisant l'API REST suivante. Cette API est accessible via l'url `<baseURL>/api/<path>`

|      <path\>    | GET | POST | PUT | DELETE |
|:---------------:|:---:|:----:|:---:|:------:|
|  nouveau/  |  /  |   /nouveau  |  /  |    /   |
|  lister/ |  /lister  |   /  |  /  |    /   |
|  editer/<int:pk>  |  /  |   /  |  /editer/<int:pk>  |    /   |
| pointsEau/<$id> |  /  |   /  |  /  |    /   |
| init/ |  /  |   /init  |  /  |    /   |

## Contribution 
1. Fork le projet et faire une PR
2. Contribuer aux points d'eau sur l'application

## Crédits 

Application propulsée dans l'espace par Lolo & Matisse


