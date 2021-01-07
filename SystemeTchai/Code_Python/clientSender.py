import re, string, sys, os
from subprocess import Popen, PIPE, STDOUT

import os
path = os.getcwd()
print(path)

def runcommand(args) :

    cmd = "curl" + args
    print('running %s' % cmd)
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    p.wait()
    output = p.communicate()[0]
    print (output)


def sign_data(private_key_loc, data):
    '''
    param: private_key_loc chemin vers le private key
    param: package Data à signé
    return: base64 encoded de la signature
    '''
    from Crypto.PublicKey import RSA 
    from Crypto.Signature import PKCS1_v1_5 
    from Crypto.Hash import SHA256 
    from base64 import b64encode, b64decode 
    key = open(private_key_loc, "r").read() 
    rsakey = RSA.importKey(key) 
    signer = PKCS1_v1_5.new(rsakey) 
    digest = SHA256.new() 
    # au cas où le message est en base64 encoded, donc il faudra decoder avant updating le digest 
    #digest.update(b64decode(data)) 
    digest.update(data)
    sign = signer.sign(digest) 
    return b64encode(sign)


datatest = "alors tu veux un message pour tester la signature"
private_key_location = path + "/../../private_key.pem"
signature = sign_data(private_key_location, datatest)
#datatest = "alors tu veux un message pour tester la "
f = open(path+'/../../signature.pem','w')
f.write(signature)
f.close()

args = " -d '{\"signPath\":" + "\"/signature.pem\"" +", \"datatest\":\"" + str(datatest) + "\"}' -H 'Content-Type: application/json'  -X POST http://0.0.0.0:898/signVerification"
runcommand(args)