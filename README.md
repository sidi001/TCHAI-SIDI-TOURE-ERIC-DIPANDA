# Goal: design an electronic transaction system with guaranteed integrity, accessible via the HTTP protocol.

Favorite way of working: pairs, **so we decided to work in pairs**
- Sidi TOURE
- Eric Landry Kotto-Dipanda

and this for both projects:
1. advanced system info ==> __who is on this git__
2. Big Data which is on the git of this link ==> [BigDataProjet](https://github.com/sidi001/Projet_BigData_LandryDipanda_SidiToure)

After completing all the exercises, we will need to obtain a management system for
transactions resembling that of blockchain and git.
Python environment, conda 3.7

## Authors
- Eric Landry Kotto Dipanda [eric-landry_kotto-dipanda@etu.u-bourgogne.fr](eric-landry_kotto-dipanda@etu.u-bourgogne.fr)
- Sidi TOURé [Sidi_Toure@etu.u-bourgogne.fr](Sidi_Toure@etu.u-bourgogne.fr)

============= finished version 0 of the project at this level==============

============= debut version 1 ==============
## Exercise 3
### A1-) recording function
#### this function is triggered with the sample script:
- curl -d '{"person1": "Robert", "person2": "Natalie", "amount":"20"}' -H "Content-Type: application/json" -X POST http://0.0 .0.0:898/save

### A2-) transaction list display:
- click on thelink: http://0.0.0.0:8981/listesTransactions

### A3-) Display a list of transactions in chronological order related to a given person (Natalie for example)
- click on the link http://0.0.0.0:8981/mes_transactions/Natalie

### A4-) Display the account balance of the given person (Natalie for example).
- click on the link http://0.0.0.0:8981/mes_soldes/Natalie

NB: the link http://0.0.0.0:8981/ used for each script or test url depends on the one through which your machine launched the code, the port number must correspond to the one with which you launched your code

## Exercise 4
### attack function, example of script to launch to trigger the method in our code for this purpose
- curl -d '{"person1": "steve", "person2": "keita", "amount":"10"}' -H "Content-Type: application/json" -X POST http://0.0 .0.0:8981/attack

message return if it works ==> "sums transactions are attacked."

============= finished version 1 of the project at this level==============

============== debut version 2 of Tchai ===========
- choice of Hash function:
    SHA-2 is a family of hash functions that were designed by the United States National Security Agency, modeled after the SHA-1 and SHA-0 functions, themselves heavily inspired by Ron Rivest's MD4 function ( which gave parallel MD5).
    In the code, we will use sha224 because it is the simplest of the other SHA-2s with the size of the hash indicated by the suffix: 224 bits for SHA-224

## Exercise 5
### Modify your program to incorporate the new transaction structure (P1, P2, t, a).
- we will put in place of the "a", the SHA224 hash defined previously

## Exercise 6
### Verify data integrity by recalculating hashes from data and comparing them with previously stored hashes.
- for this, we have set up an API accessible with the url: http://0.0.0.0:8981/integrite
- this API returns a sentence confirming that our database is correct, so we can conclude on the integrity at the same time.

## EXERCISE 7. we check that the previous attack no longer works. because the integrity test returns that the data is incorrect after the modifications

## EXERCISE 8. Attack the system by directly modifying the data file, by deleting a transaction.
- curl -d '{"person1": "Robert", "person2": "Natalie", "amount":"29"}' -H "Content-Type: application/json" -X POST http://0.0 .0.0:898/delete
============= finished version 2 of the project at this level==============

============== early version 3 of Tchai ==========

## Exercise 9
Change the hash calculation method. Now the value of the hash hi+1 so that it also depends on the hi of the transaction
former.
   - for this, we will just take into account each addition, the calculation of the hash is done using the last transaction added

## Exercise 10
To verify that the previous attacks no longer work, we check the integrity of the data (the code must first be modified to take into account the way the hash is calculated).
    - we notice that the deletion of a line triggers an incorrect data type alert in our database

## Exercise 11
 this question is quickly answered because we can already add transactions in the data without verification by already adding the method that was added in the code to question A1 of exercise 3-).

 ============= finished version 3 of the project at this level==============

 ============== early version 3 of Tchai ===========

 ## Exercise 12
    Read message [4], original paper by Satoshi Nakamoto [5] and subsequent discussion
on the diff list
