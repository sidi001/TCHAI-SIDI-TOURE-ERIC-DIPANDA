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

============= fini la version 1 du projet à ce niveau==============

============== debut version 2 de Tchai ===========
- choix fonction de Hachage:
    SHA-2 est une famille de fonctions de hachage qui ont été conçues par la National Security Agency des États-Unis, sur le modèle des fonctions SHA-1 et SHA-0, elles-mêmes fortement inspirées de la fonction MD4 de Ron Rivest (qui a donné parallèlement MD5).
    Dans le code, on utilisera le sha224 car il est le plus simple des autres SHA-2 avec la taille du haché est indiquée par le suffixe : 224 bits pour SHA-224

## Exercice 5
### Modifier votre programme afin d’intégrer la nouvelle structure des transactions (P1, P2, t, a).
- on mettra à la place du "a", le hash SHA224 defini precedemment

## Exercice 5
### Vérifier l’intégrité des données en recalculant les hashs à partir des données et en les comparant avec les hashs stockés précédemment.
- pour cela, on a mis en place un API accessible avec l'url : http://0.0.0.0:8981/integrite 
- cette api retourne une phrse nous confirmant que notre database est bien correcte, ainsi on pourra conclure sur l'integrité en même temps.

## EXERCICE 7. on verifie bien que l’attaque précédente ne fonctionne plus. car le test d'integrité retourne que les données sont incorrect après les modification

## EXERCICE 8. Attaquer le système en modifiant directement le fichier de données, en supprimant unetransaction. 
- curl -d '{"personne1": "Robert", "personne2": "Natalie", "montant":"29"}' -H "Content-Type: application/json" -X POST   http://0.0.0.0:898/supprimer

============= fini la version 2 du projet à ce niveau==============