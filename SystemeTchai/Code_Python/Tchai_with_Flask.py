from flask import *
import csv
import pandas as pd
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

@app.route('/listesTransactions')
def listesTransactions():
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
curl -d '{"personne1": "name_sender", "personne2": "name_receiver", "montant":"20"}' -H "Content-Type: application/json" -X POST   http://0.0.0.0:898/save
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
    print(date_time)
    ##a prendre en compte que la direction ci dessous particulier au pc 
    with open('./SystemeTchai/Data_Base/transactions.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(send)

    return 'tansaction : ' + ','.join(send) + ' added.\n', 201

""" focntion d\'attaque, dans notre cas, on part du principe que la personne a l\'origine de l\'attaque 
  connait et l\'expediteur et le recepteur de la transaction"""

"""
curl -d '{"personne1": "name_sender", "personne2": "name_receiver", "montant":"100"}' -H "Content-Type: application/json" -X POST   http://0.0.0.0:898/attaque
"""
@app.route('/attaque', methods=['POST'])
def attaquer():
    file_name0 = "./SystemeTchai/Data_Base/transactions.csv"
    df = pd.read_csv(file_name0, delimiter = "|")
    data = request.get_json()
    print(data)
    print(df)
    
    df.loc[(df['personne1']==str(data["personne1"])) & (df['personne2']==str(data["personne2"])),"montant"] = data["montant"]
    
    print(df)
    df.to_csv(file_name0, sep = "|")

    return 'sommes tansactions are attaqued.\n', 201




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


app.run(host='0.0.0.0',port='8981', debug=True)
print("alors quoi de neuf")
