from asym import asym_key_gen, asym_key_enc, asym_key_dec
from sym import sym_key_gen, sym_key_enc, sym_key_dec

pri_key = ''
pub_key = ''

def main():
    global pri_key
    global pub_key
    done = False
    while done == False:
        fileselectenc = False
        fileselectdec = False
        chosenenc = False
        chosendec = False
        print("Hello, welcome to the Cryptographer!")
        print("""Type in the number of one of the following options:
                1. Encrypt a text file.
                2. Decrypt a text file.
                3. Close the program.""")
        choice = input("Enter number: ")
        if choice != None:
            if choice == "1":
                print("You have chosen to encrypt a text file. Please submit you text file by typing in the name of the file.\nFor example: 'myfile.txt'. Make sure your text file has the .txt extension and is placed in the same folder as this program.")
                while fileselectenc == False:
                    filename = input("Enter filename: ")
                    try:
                        f = open(filename)
                        f.close()
                        print("Would you like to use symmetric or asymmetric encryption? Type in 's' for symmetric encryption or type in 'a' for asymmetric encryption")
                        methodenc = input("Enter 's' or 'a': ")
                        while chosenenc == False:
                            if methodenc == "s":
                                chosenenc = True
                                print("You have chosen symmetric encryption.")
                                print("""Do you want to generate a new key or use an existing one? Answer 'yes' if you would like to generate a new key.""")
                                key = input()
                                if key == "yes":
                                    print("A new key will be generated")
                                    sym_key_gen()
                                    sym_key = "key.txt"
                                else:
                                    print("Existing key will be used. Make sure all key files are in the same folder as this program.")
                                    print("What is the name of the key file? Include the .txt in the name.")
                                    sym_key = input("Enter key file name (including .txt): ")
                                print("This function has not been added yet. Try something else please.")
                                sym_key_enc(filename, sym_key)
                            elif methodenc == "a":
                                chosenenc = True
                                print("You have chosen asymmetric encryption.")
                                print("""Do you want to generate a new key or use an existing one? Answer 'yes' if you would like to generate a new key. If you already have a key, make sure it is in the PEM format. Otherwise, the key won't work.""")
                                key = input()
                                if key == "yes":
                                    print("A new key will be generated.")
                                    asym_key_gen()
                                    pri_key = "private_key.pem"
                                    pub_key = "public_key.pem"
                                else:
                                    print("What is the name of the private key file? Include the .pem in the name.")
                                    pri_key = input("Enter private key file name (including .pem): ")
                                    print("What is the name of the public key file? Include the .pem in the name.")
                                    pub_key = input("Enter public key file name (including .pem): ")
                                    print("Existing key will be used. Make sure all key files are in the same folder as this program.")
                                asym_key_enc(filename, pub_key)
                            else:
                                print("You input was invalid. Please type in 's' if you want to use symmetric encryption or type in 'a' if you want to use asymmetric encryption.")
                                continue
                        fileselectenc = True
                    except FileNotFoundError:
                        print("The chosen filename is incorrect. Please try again.")

            elif choice == "2":
                print("You have chosen to decrypt a text file. Please submit you text file by typing in the name of the file.\nFor example: 'myfile.txt'. Make sure your text file has the .txt extension and is placed in the same folder as this program.")
                while fileselectenc == False:
                    filename = input("Enter filename: ")
                    try:
                        f = open(filename)
                        f.close()
                        print("Did you use symmetric or asymmetric encryption on the file you want to decrypt now? Type in 's' if it was symmetric encryption or type in 'a' if it was asymmetric encryption.")
                        methoddec = input("Enter 's' or 'a': ")
                        while chosendec == False:
                            if methoddec == "s":
                                chosendec = True
                                print("You have chosen symmetric encryption.")
                                print("What is the name of your key file?")
                                sym_key = input("Enter file name: ")
                                sym_key_dec(filename, sym_key)
                            elif methoddec == "a":
                                chosendec = True
                                print("You have chosen asymmetric encryption.")
                                print("What is the name of your PRIVATE key file?")
                                pri_key = input("Enter file name: ")
                                asym_key_dec(filename, pri_key)
                            else:
                                print("You input was invalid. Please type in 's' if you want to use symmetric encryption or type in 'a' if you want to use asymmetric encryption.")
                                continue
                    except FileNotFoundError:
                        print("The chosen filename is incorrect. Please try again.")
            elif choice == "3":
                print("Thank you for using the Cryptographer. Until next time!")
                done = True
            else:
                print("Wrong input. Please choose between numbers 1 to 3.")
        else:
            print("You haven't typed in anything! Please try again.")

main()
