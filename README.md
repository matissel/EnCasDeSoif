[![Build Status](https://travis-ci.com/Matissou/EnCasDeSoif.svg?branch=master)](https://travis-ci.com/Matissou/EnCasDeSoif)

# EnCasDeSoif

Bienvenue sur **En cas de soif**. Cette application web permet de trouver les points d'eaux les plus proches.
Que ce soit pour boire, mettre de l'eau sur un bobo ou même se laver, cette application communautaire saura répondre à vos attentes !

## Installation 

### Avec docker
#### Prérequis
- Docker

```bash
$ docker run --rm --name EnCasDeSoif -p 8000:8000 loicrosso/en-cas-de-soif
```
> Go to localhost:8000

### Depuis les sources
#### Prérequis
- Python 3.7
- Pip

```bash
$ git clone https://github.com/Matissou/EnCasDeSoif
$ cd EnCasDeSoif
#installer les dépendances
$ pip install -r requirements.txt
# préparer la base de données
$ python manage.py makemigrations && python manage.py migrate
# lancer le serveur
$ python manage.py runserver
```

> Go to localhost:8000

## Documentation 
Voir le dossier docs/

```bash
docsify serve docs
```

> Go to localhost:3000

[//]: <> (Pour générer le tableau à partir du CSV : https://www.tablesgenerator.com/markdown_tables)
### API
Il est possible d'utiliser EnCasDeSoif en utilisant l'API REST suivante. Cette API est accessible via l'url `<baseURL>/api/<path>`

|      <path\>    | GET | POST | PUT | DELETE |
|:---------------:|:---:|:----:|:---:|:------:|
|  account/login  |  /  |   /  |  /  |    /   |
|  pointsEau/all  |  /  |   /  |  /  |    /   |
| pointsEau/<$id> |  /  |   /  |  /  |    /   |

## Contribution 
1. Fork le projet et faire une PR
2. Contribuer aux points d'eau sur l'application

## Crédits 

Application propulsée dans l'espace par Lolo & Matisse


