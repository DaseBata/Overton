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
### 1) Se mettre dans le dossier Overton_file :

- cd Overton_file

Architecture :

    /Overton_file
        /data
        /script_join.py

### 2) Executer le script qui joint les fichiers entre eux :

- py script_join.py

## Lancer le dashboard :

### 1) Se mettre dans le dossier Flask :

- cd ..
- cd Flask

Architecture :

    /Flask
        /static
        /templates
        /flask_overton.py
        /overton.jsonl
        /test.py

### 2) Faire l'une des commandes suivantes :

En restant dans le dossier Flask précédemment décrit

- py flask_overton.py

- python flask_overton.py

### 3) Affichage dans le navigateur

Faites un CTR + Clic sur l'url en dessous de la commande dans le terminal (surement juste en dessous d'un warning rouge)
