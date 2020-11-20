import cryptography, random
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

pri_key = ''
pub_key = ''

#generate keys for asymmetric method
def asym_key_gen():
    global pri_key
    global pub_key
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
    pri_key = 'private_key.pem'


    #store public key in a file
    pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open('public_key.pem', 'wb') as f:
        f.write(pem)
    pub_key = 'public_key.pem'

#asymmetric encryption function
def asym_key_enc(filename):
    global pub_key
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
def asym_key_dec(filename):
    global pri_key
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




def main():
    global pri_key
    global pub_key
    done = False
    while done == False:
        print("Hello, welcome to the Cryptographer!")
        print("""Type in the number of one of the following options:
                1. Encrypt a text file.
                2. Decrypt a text file.
                3. Close the program.""")
        choice = input("Enter number: ")
        if choice != None:
            if choice == "1":
                print("You have chosen to encrypt a text file. Please submit you text file by typing in the name of the file.\nFor example: 'myfile.txt'. Make sure your text file has the .txt extension and is placed in the same folder as this program.")
                filename = input("Enter filename: ")
                if filename != None:
                    #method = randint(0, 1)
                    method = 1
                    if method == "0":
                        print("""Do you want to generate a new key or use an existing one? Answer 'yes' if you would like to generate a new key.""")
                        key = input()
                        if key == "yes":
                            print("A new key will be generated")
                            #sym_key_gen()
                        else:
                            print("Existing key will be used. Make sure all key files are in the same folder as this program.")
                        print("This function has not been added yet. Try something else please.")
                        #sym_key_enc(filename)
                    else:
                        print("""Do you want to generate a new key or use an existing one? Answer 'yes' if you would like to generate a new key. If you already have a key, make sure it is in the PEM format. Otherwise, the key won't work.""")
                        key = input()
                        if key == "yes":
                            print("A new key will be generated.")
                            asym_key_gen()
                        else:
                            print("What is the name of the private key? Include the .pem in the name.")
                            pri_key = input("Enter private key name (including .pem): ")
                            print("What is the name of the public key? Include the .pem in the name.")
                            pub_key = input("Enter public key name (including .pem): ")
                            print("Existing key will be used. Make sure all key files are in the same folder as this program.")
                        asym_key_enc(filename)
                else:
                    print("The filename you have submitted is incorrect or the file itself is not in the folder. Make sure you have typed the name correctly")
                    break
            elif choice == "2":
                print("You have chosen to decrypt a text file. Please submit you text file by typing in the name of the file.\nFor example: 'myfile.txt'. Make sure your text file has the .txt extension and is placed in the same folder as this program.")
                filename = input("Enter filename: ")
                if filename != None:
                    #method = randint(0, 1)
                    method = 1
                    if method == "0":
                        print("This function has not been added yet. Try something else please.")
                        #sym_key_dec(filename)
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

main()
