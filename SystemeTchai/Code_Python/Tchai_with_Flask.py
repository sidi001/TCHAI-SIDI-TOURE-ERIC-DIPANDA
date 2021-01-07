from flask import *
import csv
import pandas as pd
from datetime import datetime
import hashlib

import os
path = os.getcwd()
print(path)

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
Robert|Natalie|22|12/21/2020, 15:24:48|f36e498739b755a704dfe52ca12f988250a43d2cfcdf1cc601a7dc87
Bernard|Robert|37|12/21/2020, 15:26:03|77cfd7f5b0d4b068d8ea28391e04e59e365bc4623e57c31082613cd6
Natalie|Bernard|29|12/21/2020, 15:26:30|2f230c031e1c44c059caa16f4c1e87fca060d3fc22672910dd304765
linuxize|linuxize@example.com|20|12/21/2020, 15:27:05|54a05e679466f0efd5999457bbb939a43012b172d778b3cc8d34db3b
linuxize|linuxize@example.com|20|12/21/2020, 15:27:10|00541f12b9bccbd3c15e2bf4b031603c85cc17e05a761aec4f3f3909
steve|keita|20|12/21/2020, 15:27:39|9e5333d0e667242fee03f6a6e49b4bafc10f587f9e52775a1337b793
curl -d '{"personne1": "Robert", "personne2": "Natalie", "montant":"22"}' -H "Content-Type: application/json" -X POST   http://0.0.0.0:8981/save
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
    transaction = []
    with open('./SystemeTchai/Data_Base/transactions.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='|')
        for row in spamreader:
            transaction = row
        print(transaction)
        hi = transaction[4]
    h = hashlib.sha224(",".join(send) + hi).hexdigest()
    send.append(h)
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
    df.to_csv(file_name0, sep = "|", index_col = False)

    return 'sommes tansactions are attaqued.\n', 201

"""
curl -d '{"personne1": "Robert", "personne2": "Natalie", "montant":"29"}' -H "Content-Type: application/json" -X POST   http://0.0.0.0:898/supprimer
"""
@app.route('/supprimer', methods=['POST'])
def supprimer():
    file_name0 = "./SystemeTchai/Data_Base/transactions.csv"
    transactions = []
    data = request.get_json()
    with open('./SystemeTchai/Data_Base/transactions.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='|')
        for row in spamreader:
            if row[0]=='personne1' :
                 continue
            
            if row[0]==str(data["personne1"]) and row[1]==str(data["personne2"]) and str(row[2])==str(data["montant"]) :
                continue

            transactions.append(row)
        
        df = pd.DataFrame(transactions, columns=["personne1","personne2","montant","date","hash"])

    df.to_csv(file_name0, index = False, sep = "|", columns=None)

    return 'sommes tansactions are removed.\n', 201




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

@app.route('/integrite', methods=['GET'])
def integrite():
    data = "correct"
    with open('./SystemeTchai/Data_Base/transactions.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='|')
        for row in spamreader:
            if row[0]=='personne1' :
                hi = row[4]
                continue

            
            h = hashlib.sha224( ",".join(row[0:4]) + hi).hexdigest()
            if h != row[4] :
                data = "incorrect"
            hi = row[4]


    return 'les donnees sont actuellemnt ' + str(data), 200


@app.route('/signVerification', methods=['POST'])
def verifier_signature():
    '''
    Verifier avec le public key a partir d'où vient la signature cela permet d'avoir une coherence avec le private key
    Postjson param: public_key_loc est chemin du public key
    Postjson param: signature String signature to be verified
    return: message."les donnees envoyees sont bien verifiees" si la signature est valid; "les donnees sont faux" sinon. 
    '''

    public_key_loc = path + "/public_key.pem"

    data = request.get_json()
    signPath =  path + str(data["signPath"])
    sign = open(signPath, "r").read() 
    dataSended = str(data["datatest"])
    
    from Crypto.PublicKey import RSA 
    from Crypto.Signature import PKCS1_v1_5 
    from Crypto.Hash import SHA256 
    from base64 import b64decode 
    pub_key = open(public_key_loc, "r").read() 
    rsakey = RSA.importKey(pub_key) 
    signer = PKCS1_v1_5.new(rsakey) 
    digest = SHA256.new() 
    # if Assumes the data is base64 encoded to begin with
    #digest.update(b64decode(data)) 
    digest.update(dataSended) 
    if signer.verify(digest, b64decode(sign)):
        return "les donnees envoyees sont bien verifiees"
    return "les donnees sont faux"



app.run(host='0.0.0.0',port='898', debug=True)
print("alors quoi de neuf")
