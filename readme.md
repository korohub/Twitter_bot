## Twitter Bot



[<img src="https://www.gercekgundem.com/images/posts/202006/209718_814x458.jpg">](http://google.com.au/)


Permet de poster sur twitter en utilisant l'api twitter et tweepy.
Les données sont proviennet d'une base de données Mongodb.
Génération d'une image avec pillow et ajout du texte dessus.


## Pour commencer

Git clone https://github.com/korohub/Twitter_bot.git


### Pré-requis

Ce qu'il est requis pour commencer avec votre projet...

- APScheduler==3.8.0
- certifi==2021.5.30
- charset-normalizer==2.0.6
- click==8.0.1
- colorama==0.4.4
- Flask==2.0.1
- idna==3.2
- itsdangerous==2.0.1
- Jinja2==3.0.1
- MarkupSafe==2.0.1
- numpy==1.21.2
- oauthlib==3.1.1
- Pillow==8.3.2
- pymongo==3.12.0
- pytz==2021.1
- requests==2.26.0
- requests-oauthlib==1.3.0
- six==1.16.0
- tweepy==4.0.0
- tzlocal==2.1
- urllib3==1.26.7
- Werkzeug==2.0.1


### Installation

Les étapes pour installer 

cd twitter_bot

Avec venv :
```
python -m venv venv
pip install -r requirements.txt
```

Avec pipenv :
```
pipenv install -r requirements.txt
```

Avec pip:
```
pip install -r requirements.txt
```

## Démarrage

Le script peut fonctionner en local en lui passant un paramètre de votre choix.
ou en l'exécutant depuis un conteneur docker via tâche cron ou jenkins.( Mon choix)

```sh
python app.py ( args optionnal)
```





## Versions

_exemple :_
**Dernière version stable :** 1.0
**Dernière version :** 1.0


## Auteurs
Listez le(s) auteur(s) du projet ici !
* _**Moi**_

## Todo

- Génération image avec gradient dynamique => Gradient.py 
- 
