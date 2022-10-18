# Python_AIMATCH

##  EasyDate est un site de rencontre qui organise des speed dating.Les participants remplissent un formulaire avec différentes informations sur eux. L'objectif étant de voir ceux qui match ensemble
##  AI match est notre équipe data scientoist qui doit réfléchir à un modèle permettant de prédire si deux personnes vont matcher selon le formulaire complété préalablement de la rencontre.

### Ce projet comporte deux grandes parties: la partie prédiction et la partie data visualisation.
## Première partie: Prédiction
### La prédiction se trouve dans le fichier prediction.py.
### Tout d'abord nous avons nettoyer la base de données avec la méthode les K plus proches voisins pour les variables quantitatives et par le mode pour les variables quantitatives. Nous avons appliqué l'arbre de decision pour recuperer les variables importantes à mettre dans le modèle. Les données étant des données déséquilibrées nous avons appliquons smote d'une part et d'autre part Sborderline Smote. Nous appliquons plusieurs modèles  soit sur  les données déséquilibrées soit sur les données équilibrées. Pour chaque modèle il y a la partie application du modèle sur les données d'apprentissage, ensuite la prédiction sur les données test et l'évaluation du modèle avec comme critère le F1_score.



## Deuxième partie : Application

### Le lien de l'application 
<a href="https://aimatch69.herokuapp.com/" target="_blank">Dashboard hébergé sur Heroku</a>
