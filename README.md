# Objectif : concevoir un système de transactions électroniques avec une intégrité garantie, accessible par le protocole HTTP.

Mode du travail préférée : binômes, **ainsi nous avons decidé de travailler en binôme**
- Sidi TOURÉ
- Eric Landry Kotto-Dipanda

et cela pour les deux projets:
1. système d'information avancée ==> __qui est sur ce git__
2. Big Data qui se trouve sur le git de ce lien ==> [BigDataPrjet](https://github.com/sidi001/Projet_BigData_LandryDipanda_SidiToure)

Après avoir terminé tous les exercices, nous devrons obtenir un système de gestion des
transactions ressemblant à celui de la blockchain et git.

## Auteurs
- EricLandry Kotto Dipanda [eric-landry_kotto-dipanda@etu.u-bourgogne.fr](eric-landry_kotto-dipanda@etu.u-bourgogne.fr)
- Sidi TOURé [Sidi_Toure@etu.u-bourgogne.fr](Sidi_Toure@etu.u-bourgogne.fr)

============= fini la version 0 du projet à ce niveau==============

============= debut la version 1 ==============
## Exercice 3
### A1-) fonction d'enregistrement
#### cette fonction est declenché avec l'exemple de script :
- curl -d '{"personne1": "steve", "personne2": "keita", "montant":"27"}' -H "Content-Type: application/json" -X POST   http://0.0.0.0:898/save

### A2-) affichage liste transactions :
- lancer le lien http://0.0.0.0:8981/listesTransactions

### A3-) Afficher une liste des transactions dans l’ordre chronologique liées à une personne donnée  (Natalie par exemple)
- lancer le lien http://0.0.0.0:8981/mes_transactions/Natalie

### A4-) Afficher le solde du compte de la personne donnée (Natalie par exemple).
- lancer le lien http://0.0.0.0:8981/mes_soldes/Natalie

NB: le lien http://0.0.0.0:8981/ utilisé pour chaque script ou url de teste depend de celui par lequel votre machine a lancer le code, le numero du port doit correspondre à celui avec lequel vous avez lancé votre code

## Exercice 4
### fonction d'attaque, exemple de script a lancer pour declencher la methode dans notre code à cet effet
- curl -d '{"personne1": "steve", "personne2": "keita", "montant":"10"}' -H "Content-Type: application/json" -X POST   http://0.0.0.0:8981/attaque

message retourner si ça marche ==> "sommes tansactions are attaqued."
