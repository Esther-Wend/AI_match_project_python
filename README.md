# Python_AIMATCH  
![Alt Text](https://media.giphy.com/media/eft1vx8J4SPUiWxfc4/giphy.gif)


##  EasyDate est un site de rencontre qui organise des speed dating. Les participants remplissent un formulaire avec différentes informations sur eux. L'objectif étant de voir ceux qui match ensemble.
##  AI match est notre équipe data scientist qui doit réfléchir à un modèle permettant de prédire si deux personnes vont matcher selon le formulaire complété préalablement à la rencontre.

### Ce projet comporte deux grandes parties: la partie prédiction et la partie data visualisation.

## Première partie: Prédiction

### La prédiction se trouve dans le fichier prediction.py.
### Tout d'abord  la base de données a été nettoyée  avec la méthode des K plus proches voisins pour les variables quantitatives et par le mode pour les variables qualitatives. Ensuite  l'arbre de decision  a été appliqué pour selectionner les variables importantes à mettre dans le modèle. Les données étant des données déséquilibrées nous avons appliqué smote d'une part et d'autre part Sborderline Smote. Plusieurs modèles ont été utilisés, soit sur les données déséquilibrées soit sur les données équilibrées. Pour chaque modèle il y a la partie application du modèle sur les données d'apprentissage, ensuite la prédiction sur les données test et l'évaluation du modèle avec comme critère le F1_score. Le meilleure modèle est sauvegardé en format pickle.



## Deuxième partie : Application
### L'objectif du tableau de bord est de permettre à l'utilisateur d'interagir sur les données, de pouvoir voir le profil des utilisateurs et d'utiliser le modèle prédictif. L'application est basée sur 4 script: l'app.py , le data.py , l'index.py et le layout.py. L'application comporte un menu accueil qui presente l'objectif du projet et l'entreprise AI match, un menu analyse où se trouve les différents graphiques interactifs interessants, un menu  profil des participants. 


## Fonctionnalité en cours de développement
### Projection régression  qui devait contenir la prédiction.
### Tester les données servira à déposer un fichier pour prédire si deux profil match ou pas.


## Le lien de l'application 
<a href="https://aimatch69.herokuapp.com/" target="_blank">Dashboard hébergé sur Heroku</a>
