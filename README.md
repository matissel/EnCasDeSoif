[![Build Status](https://travis-ci.com/Matissou/EnCasDeSoif.svg?branch=master)](https://travis-ci.com/Matissou/EnCasDeSoif)

# EnCasDeSoif

Bienvenue sur **En cas de soif**. Cette application web permet de trouver les points d'eaux les plus proches.
Que ce soit pour boire, mettre de l'eau sur un bobo ou même se laver, cette application communautaire saura répondre à vos attentes !

## Installation 

```bash
python manage.py runserver
```

> Go to localhost:8000


[//]: <> (Pour générer le tableau à partir du CSV : https://www.tablesgenerator.com/markdown_tables)
#### API
Il est possible d'utiliser EnCasDeSoif en utilisant l'API REST suivante. Cette API est accessible via l'url `<baseURL>/api/<path>`

|      <path\>    | GET | POST | PUT | DELETE |
|:---------------:|:---:|:----:|:---:|:------:|
|  nouveau/  |  /  |   /nouveau  |  /  |    /   |
|  lister/ |  /lister  |   /  |  /  |    /   |
|  editer/<int:pk>  |  /  |   /  |  /editer/<int:pk>  |    /   |
| pointsEau/<$id> |  /  |   /  |  /  |    /   |
| init/ |  /  |   /init  |  /  |    /   |

### Contribution 
1. Fork le projet et faire une PR
2. Contribuer aux points d'eau sur l'application

### Crédits 

Application propulsée dans l'espace par Lolo & Matisse


