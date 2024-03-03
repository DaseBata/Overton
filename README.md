# Prérequis

Les instructions suivantes doivent être effectuées dans un terminal

## Faire les installations des packages nécessaires :

- pip install jsonlines
- pip install os
- pip install flask
- pip install plotly
- pip install pandas

## Installer git et cloner le dépot GIT :

- git clone https://github.com/DaseBata/Overton

## Mettre les données en forme pour le dashBoard :
### 1) Se mettre dans le dossier Flask du dossier Overton :

- cd Overton/Flask

Architecture Overton :

    /Overton
        /Flask
        /README.md

Architecture Flask :

    /Flask
        /data
        /static
        /templates
        /flask_overton.py
        /script_join.py


### 2) Faire l'une des commandes suivantes pour joindre les fichiers du dossier data en un seul :

- py script_join.py
- python script_join.py

## Lancer le dashboard :

### 1) Faire l'une des commandes suivantes :

En restant dans le dossier Flask précédemment décrit

- py flask_overton.py

- python flask_overton.py

### 2) Affichage dans le navigateur

Faites un CTR + Clic sur l'url en dessous de la commande dans le terminal (surement juste en dessous d'un warning rouge)

Ex :

<span style="color: #FF0000">WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.</span>\
\* Running on http://127.0.0.1:5000
