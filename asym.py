import cryptography, random
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

#generate keys for asymmetric method
def asym_key_gen():
    #generate private and public key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    #store private key in a file
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open('private_key.pem', 'wb') as f:
        f.write(pem)


    #store public key in a file
    pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open('public_key.pem', 'wb') as f:
        f.write(pem)

#asymmetric encryption function
def asym_key_enc(filename, public):
    pub_key = public
    #read public key for encryption
    with open(pub_key, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

    #read file and encrypt contents
    f = open(filename, 'rb')
    message = f.read()    
    f.close()
    
    encrypted = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    #write encrypted contents to file
    f = open(filename, 'wb')
    f.write(encrypted)
    f.close()
    print("Your file has been encrypted succesfully.")

#asymmetric decryption function
def asym_key_dec(filename, private):
    filename = filename
    pri_key = private
    #read encrypted file and decrypt contents
    f = open(filename, 'rb')
    encrypted = f.read()
    f.close()
    with open(pri_key, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    original_message = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    #write decrypted contents to file
    f = open(filename, 'wb')
    f.write(original_message)
    f.close()
    print("Your file has been decrypted succesfully.")