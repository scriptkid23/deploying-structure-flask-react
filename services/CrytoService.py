from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode, b64encode

class CryptoService:
    public_key = None
    private_key = None 

    def __init__(self):
        with open("key/public.pem","rb") as f:
            self.public_key = RSA.import_key(f.read())
        with open("key/private.pem","rb") as f:
            self.private_key = RSA.import_key(f.read())

    def encrypt(self,message):
        cipher  = PKCS1_OAEP.new(self.public_key)
        return b64encode(cipher.encrypt(message.encode())).decode("utf-8")
    def decrypt(self,message):
        decipher = PKCS1_OAEP.new(self.private_key)
        return decipher.decrypt(b64decode(message)).decode("utf-8")