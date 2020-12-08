from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def sym_key_gen():
    key = Fernet.generate_key()
    print("Please enter a password to secure your key:")

    with open('key1.txt', 'wb') as f:
        f.write(key)

def sym_key_enc(filename):
    k = open("key1.txt", 'rb')
    key = k.read()
    m = open(filename, 'rb')
    message = m.read()
    f = Fernet(key)
    token = f.encrypt(message)

    w = open(filename, 'wb')
    w.write(token)
    w.close()
    print("Your file has been encrypted succesfully.")

def sym_key_dec(filename):
    k = open("key1.txt", 'rb')
    key = k.read()
    m = open(filename, 'rb')
    message = m.read()
    f = Fernet(key)
    token = f.decrypt(message)

    w = open(filename, 'wb')
    w.write(token)
    w.close()
    print("Your file has been decrypted succesfully.")






