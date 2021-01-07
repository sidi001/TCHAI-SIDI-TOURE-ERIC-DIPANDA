import os
path = os.getcwd()
print(path)

def generate_RSA(bits=2048):
    '''
    Generate an RSA keypair with an exponent of 65537 in PEM format
    param: bits The key length in bits
    Return private key and public key
    '''
    from Crypto.PublicKey import RSA 
    new_key = RSA.generate(bits, e=65537) 
    public_key = new_key.publickey().exportKey("PEM") 
    private_key = new_key.exportKey("PEM") 
    
    return private_key, public_key


private_key, public_key = generate_RSA(2048)
f = open(path+'/private_key.pem','w')
f.write(private_key)
f.close()

f = open(path+'/public_key.pem','w')
f.write(public_key)
f.close()

print(private_key)
