from flask import *
import csv
import pandas
from datetime import datetime

# import os
# path = os.getcwd()
# print(path)

app = Flask(__name__)
# transactions = ['Zorro','sidi','h']
transactions = []


@app.route('/')
def hello():
    transactions = []
    with open('./SystemeTchai/Data_Base/transactions.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='|')
        for row in spamreader:
            # if row[0]=='personne1' :
            #     continue

            transactions.append(row)
            print(transactions)

    return 'toutes les transactions <ul>' + ''.join(
        ['<li> ' + ', '.join(n) for n in transactions]
    ) + '</ul>\n', 200

"""
curl -d '{"personne1": "name_sender", "personne2": "name_receiver", "montant":"20"}' -H "Content-Type: application/json" -X POST   http://0.0.0.0:898/save/
"""
@app.route('/save', methods=['POST'])
def add():
    send = []
    data = request.get_json()
    now = datetime.now() 
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    send.append(data["personne1"])
    send.append(data["personne2"])
    send.append(data["montant"])
    send.append(date_time)
    ##a prendre en compte que la direction ci dessous particulier au pc 
    with open('/Users/siditoure/Desktop/esirem/S9/systeme_d_info_avancee_SK/TCHAI-SIDI-TOURE-ERIC-DIPANDA/SystemeTchai/Data_Base/transactions.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(send)

    return 'tansaction : ' + ','.join(send) + ' added.\n', 201


@app.route('/mes_transactions/<uname>', methods=['GET'])
def mes_transactions(uname):
    transactions = []
    with open('./SystemeTchai/Data_Base/transactions.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='|')
        for row in spamreader:
            if row[0]==uname :
                transactions.append(row)
            print(transactions)

    return 'Mes transactions <ul>' + ''.join(
        ['<li> ' + ', '.join(n) for n in transactions]
    ) + '</ul>\n', 200

@app.route('/mes_soldes/<uname>', methods=['GET'])
def mes_soldes(uname):
    solde = 0
    with open('./SystemeTchai/Data_Base/transactions.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='|')
        for row in spamreader:
            if row[0]==uname :
                solde -= int(row[2])
            if row[1]==uname :
                solde += int(row[2])

    return 'Mon Solde est : <ul>' + ''.join(
        ['<li> ' + str(solde)]
    ) + '</ul>\n', 200


app.run(host='0.0.0.0',port='898', debug=True)
print("alors quoi de neuf")
