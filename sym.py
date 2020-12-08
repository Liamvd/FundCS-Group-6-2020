from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def sym_key_gen():
    key = Fernet.generate_key()
    print("Your key is stored in file 'key.txt'. Make sure to keep this file safe and don't share it with others except for those that need to encrypt your file.")

    with open('key.txt', 'wb') as f:
        f.write(key)

def sym_key_enc(filename, symkey):
    sym_key = symkey
    k = open(sym_key, 'rb')
    key = k.read()
    m = open(filename, 'rb')
    message = m.read()
    f = Fernet(key)
    token = f.encrypt(message)

    w = open(filename, 'wb')
    w.write(token)
    w.close()
    print("Your file has been encrypted succesfully.")

def sym_key_dec(filename, symkey):
    sym_key = symkey
    k = open(sym_key, 'rb')
    key = k.read()
    m = open(filename, 'rb')
    message = m.read()
    f = Fernet(key)
    token = f.decrypt(message)

    w = open(filename, 'wb')
    w.write(token)
    w.close()
    print("Your file has been decrypted succesfully.")






