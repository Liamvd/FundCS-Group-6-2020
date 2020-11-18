import cryptography, random
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def asym_key_enc(filename):
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

    #encrypt file with public key
    with open("public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

    f = open('t1.txt', 'rb')
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
    f = open('encrypted.txt', 'wb')
    f.write(encrypted)
    f.close()

def asym_key_dec(filename):
    f = open('encrypted.txt', 'rb')
    encrypted = f.read()
    f.close()
    with open("private_key.pem", "rb") as key_file:
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
    f = open('decrypted.txt', 'wb')
    f.write(original_message)
    f.close()





done = False
while done == False:
    print("Hello, welcome to the Cryptographer!")
    print("""Type in the number of one of the following options:
            1. Encrypt a text file.
            2. Decrypt a text file.
            3. Close the program.""")
    choice = input("Enter number...")
    if choice != None:
        if choice == "1":
            print("You have chosen to encrypt a text file. Please submit you text file by typing in the name of the file.\nFor example: 'myfile.txt'. Make sure your text file has the .txt extension and is placed in the same folder as this program.\nIf you want to do something else just hit enter and you will be sent back to the previous window.")
            filename = input("Enter filename...")
            if filename != None:
                print("Your file has been encrypted succesfully.")
                #method = randint(0, 1)
                method = 1
                if method == "0":
                    #symmetric method is implemented here
                    sym_key_enc(filename)
                else:
                    asym_key_enc('filename')
            else:
                break
        elif choice == "2":
            print("You have chosen to decrypt a text file. Please submit you text file by typing in the name of the file.\nFor example: 'myfile.txt'. Make sure your text file has the .txt extension and is placed in the same folder as this program.\nIf you want to do something else just hit enter and you will be sent back to the previous window.")
            filename = input("Enter filename...")
            if filename != None:
                print("Your file has been decrypted succesfully.")
                #method = randint(0, 1)
                method = 1
                if method == "0":
                    #symmetric method is implemented here
                    sym_key_dec(filename)
                else:
                    asym_key_dec(filename)
            else:
                break
        elif choice == "3":
            print("Thank you for using the Cryptographer. Until next time!")
            done = True
        else:
            print("Wrong input. Please choose between numbers 1 to 3.")
    else:
        print("You haven't typed in anything! Please try again.")

