# Objectif : concevoir un système de transactions électroniques avec une intégrité garantie, accessible par le protocole HTTP.

Mode du travail préférée : binômes, **ainsi nous avons decidé de travailler en binôme**
- Sidi TOURÉ
- Eric Landry Kotto-Dipanda

et cela pour les deux projets:
1. système d'information avancée ==> __qui est sur ce git__
2. Big Data qui se trouve sur le git de ce lien ==> [BigDataPrjet](https://github.com/sidi001/Projet_BigData_LandryDipanda_SidiToure)

Après avoir terminé tous les exercices, nous devrons obtenir un système de gestion des
transactions ressemblant à celui de la blockchain et git.
Environnement python, conda 3.7

## Auteurs
- EricLandry Kotto Dipanda [eric-landry_kotto-dipanda@etu.u-bourgogne.fr](eric-landry_kotto-dipanda@etu.u-bourgogne.fr)
- Sidi TOURé [Sidi_Toure@etu.u-bourgogne.fr](Sidi_Toure@etu.u-bourgogne.fr)

============= fini la version 0 du projet à ce niveau==============

============= debut la version 1 ==============
## Exercice 3
### A1-) fonction d'enregistrement
#### cette fonction est declenché avec l'exemple de script :
- curl -d '{"personne1": "Robert", "personne2": "Natalie", "montant":"20"}' -H "Content-Type: application/json" -X POST   http://0.0.0.0:898/save

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

## Exercice 6
### Vérifier l’intégrité des données en recalculant les hashs à partir des données et en les comparant avec les hashs stockés précédemment.
- pour cela, on a mis en place un API accessible avec l'url : http://0.0.0.0:8981/integrite 
- cette api retourne une phrse nous confirmant que notre database est bien correcte, ainsi on pourra conclure sur l'integrité en même temps.

## EXERCICE 7. on verifie bien que l’attaque précédente ne fonctionne plus. car le test d'integrité retourne que les données sont incorrect après les modification

## EXERCICE 8. Attaquer le système en modifiant directement le fichier de données, en supprimant unetransaction. 
- curl -d '{"personne1": "Robert", "personne2": "Natalie", "montant":"29"}' -H "Content-Type: application/json" -X POST   http://0.0.0.0:898/supprimer

============= fini la version 2 du projet à ce niveau==============

============== debut version 3 de Tchai ===========

## Exercice 9
Modifier la méthode de calcul de hash. Maintenant la valeur du hash hi+1 pour que ça depende aussi du hi de la transaction
précédente. 
   - pour cela, on prendra juste en compte à chaque ajout, le calcule du hash est fait en utilisant la dernière transaction ajoutée

## Exercice 10
Pour Vérifier que les attaques précédentes ne fonctionnent plus, on verifie l'integrité des données (le code doit être d'abord modifié pour prendre en compte la façon de calcul du hash).
    - on remarque bien que la suppression d'une ligne declenche une alerte de type données incorrect dans notre database

## Exercice 11
 cette question est vite repondu car on peut déjà ajouter des transactions dans les données sans verification par déjà la méthode d'ajout qui a été ajouté dans le code à la question A1 de l'exercice 3-).

 ============= fini la version 3 du projet à ce niveau==============

 ============== debut version 3 de Tchai ===========

 ## Exercice 12
    Lire le message [4], le papier original de Satoshi Nakamoto [5] et la discussion ultérieure
sur la liste de diffusion ‘The Cryptography and Cryptography Policy Mailing List”.

## Exercice 13 : crytography asymetrique, crypto.signature
    -  Utiliser la cryptographie asymétrique afin d’assurer l’authenticité de l’expéditeur.
    - pour cela, on a utilisé la bibliothèque pyCrypto de python. PyCryptodome est un package Python autonome de primitives cryptographiques de bas niveau. cela permet de d'envoyer un message signé avec une signature générée avec une clé privée, puis on envoie le message vers le server avec la signature pour proceder à une verification.
#### Procedure pour tester :
1. exécuter le code python generateRsa.py afin de générer les clés privées et public qui seront stocker dans des fichier ".pem". 
2. on peut lancer le code python testerCrypto.py pour juste savoir est ce que le model de crypto asymetrique qu'on utilise est correct.
3. Ensuite on peut lancer le code clientSender.py qui se chargera de signer un message qu'on veut envoyer en mettant la signature dans fichier de stockage et lance un script de type  "curl -d '{"signPath":"signature.pem", "datatest":"alors tu veux un message pour tester la signature"}' -H 'Content-Type: application/json'  -X POST http://0.0.0.0:898/signVerification" dont signPath contient le chemin vers la signature et datatest contient le message même.
4. ce script nous retourne "les donnees envoyees sont bien verifiees" si le message n'a pas été modifier avant la verification, donc sur le chemin de l'envoie et retourne "les donnees sont faux" sinon

 ============= fini la version 4 du projet à ce niveau==============