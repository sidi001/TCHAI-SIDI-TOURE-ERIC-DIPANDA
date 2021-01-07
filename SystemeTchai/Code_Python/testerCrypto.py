import re, string, sys, os
from subprocess import Popen, PIPE, STDOUT

def runcommand(args) :

    cmd = "curl" + args
    print('running %s' % cmd)
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    p.wait()
    output = p.communicate()[0]
    print (output)


def sign_data(private_key_loc, data):
    '''
    param: private_key_loc Path to your private key
    param: package Data to be signed
    return: base64 encoded signature
    '''
    from Crypto.PublicKey import RSA 
    from Crypto.Signature import PKCS1_v1_5 
    from Crypto.Hash import SHA256 
    from base64 import b64encode, b64decode 
    key = open(private_key_loc, "r").read() 
    rsakey = RSA.importKey(key) 
    signer = PKCS1_v1_5.new(rsakey) 
    digest = SHA256.new() 
    # It's being assumed the data is base64 encoded, so it's decoded before updating the digest 
    #digest.update(b64decode(data)) 
    digest.update(data)
    sign = signer.sign(digest) 
    return b64encode(sign)

def verifier_signature(sign, data):
    '''
    Verifies with a public key from whom the data came that it was indeed 
    signed by their private key
    param: public_key_loc Path to public key
    param: signature String signature to be verified
    return: Boolean. True if the signature is valid; False otherwise. 
    '''

    public_key_loc = "./../../public_key.pem"
    
    from Crypto.PublicKey import RSA 
    from Crypto.Signature import PKCS1_v1_5 
    from Crypto.Hash import SHA256 
    from base64 import b64decode 
    pub_key = open(public_key_loc, "r").read() 
    rsakey = RSA.importKey(pub_key) 
    signer = PKCS1_v1_5.new(rsakey) 
    digest = SHA256.new() 
    # # au cas où le message est en base64 encoded, donc il faudra decoder avant updating le digest 
    #digest.update(b64decode(data)) 
    digest.update(data) 
    if signer.verify(digest, b64decode(sign)):
        return "les donnees envoyees sont bien verifiees"
    return "les donnees sont faux"



datatest = "alors tu veux un message pour tester la signature"
private_key_location = "./../../private_key.pem"
signature = sign_data(private_key_location, datatest)
#args=" http://0.0.0.0:898/signVerification/"+signature+"/"+datatest 
#runcommand(args)
datatest = "alors tu veux un message pour tester la signatureok"
verifier_signature(signature, datatest)