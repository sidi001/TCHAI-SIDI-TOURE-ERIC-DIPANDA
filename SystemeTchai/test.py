from flask import *
import csv
app = Flask(__name__)
#names = ['Zorro','sidi','h']
names = []

@app.route('/')
def hello():
    names = []
    with open('text.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            for c in row:
                names.append(c)
            print(names)

    return 'Hello <ul>' + ''.join(
    ['<li> ' + n for n in names]
    ) + '</ul>\n', 200
@app.route('/user/<uname>', methods=['PUT'])
def add(uname):
    names.append(uname)
    with open('text.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(names)

    return 'User ' + uname + ' added.\n', 201
@app.route('/user/<uname>', methods=['DELETE'])
def rem(uname):
    names = []
    with open('text.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            for c in row:
                names.append(c)
            print(names)

    if uname not in names:
        return 'User ' + uname + ' does not exists.\n', 404
    names.remove(uname)

    with open('text.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(names)

    return 'User ' + uname + 'removed.\n', 200
    
app.run(host='0.0.0.1', debug=True)
print("alors quoi de neuf")
