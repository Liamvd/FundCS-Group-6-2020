from asym import asym_key_gen, asym_key_enc, asym_key_dec
from sym import sym_key_gen, sym_key_enc, sym_key_dec

pri_key = ''
pub_key = ''

def main():
    global pri_key
    global pub_key
    done = False
    chosen = False
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
                    print("Would you like to use symmetric or asymmetric encryption? Type in 's' for symmetric encryption or type in 'a' for asymmetric encryption")
                    method = input("Enter 's' or 'a': ")
                    while chosen == False:
                        if method == "s":
                            chosen = True
                            print("You have chosen symmetric encryption.")
                            print("""Do you want to generate a new key or use an existing one? Answer 'yes' if you would like to generate a new key.""")
                            key = input()
                            if key == "yes":
                                print("A new key will be generated")
                                sym_key_gen()
                            else:
                                print("Existing key will be used. Make sure all key files are in the same folder as this program.")
                            print("This function has not been added yet. Try something else please.")
                            sym_key_enc(filename)
                        elif method == "a":
                            chosen = True
                            print("You have chosen asymmetric encryption.")
                            print("""Do you want to generate a new key or use an existing one? Answer 'yes' if you would like to generate a new key. If you already have a key, make sure it is in the PEM format. Otherwise, the key won't work.""")
                            key = input()
                            if key == "yes":
                                print("A new key will be generated.")
                                asym_key_gen()
                                pri_key = "private_key.pem"
                                pub_key = "public_key.pem"
                            else:
                                print("What is the name of the private key? Include the .pem in the name.")
                                pri_key = input("Enter private key name (including .pem): ")
                                print("What is the name of the public key? Include the .pem in the name.")
                                pub_key = input("Enter public key name (including .pem): ")
                                print("Existing key will be used. Make sure all key files are in the same folder as this program.")
                            asym_key_enc(filename, pub_key)
                        else:
                            print("You input was invalid. Please type in 's' if you want to use symmetric encryption or type in 'a' if you want to use asymmetric encryption.")
                            continue
                else:
                    print("You haven't chosen any file, the program will abort.")
                    break
            elif choice == "2":
                print("You have chosen to decrypt a text file. Please submit you text file by typing in the name of the file.\nFor example: 'myfile.txt'. Make sure your text file has the .txt extension and is placed in the same folder as this program.")
                filename = input("Enter filename: ")
                if filename != None:
                    print("Did you use symmetric or asymmetric encryption on the file you want to decrypt now? Type in 's' if it was symmetric encryption or type in 'a' if it was asymmetric encryption.")
                    method = input("Enter 's' or 'a': ")
                    while chosen == False:
                        if method == "s":
                            chosen = True
                            print("You have chosen symmetric encryption.")
                            sym_key_dec(filename)
                        elif method == "a":
                            chosen = True
                            print("You have chosen asymmetric encryption.")
                            asym_key_dec(filename, pri_key)
                        else:
                            print("You input was invalid. Please type in 's' if you want to use symmetric encryption or type in 'a' if you want to use asymmetric encryption.")
                            continue
                else:
                    print("You haven't chosen any file, the program will abort.")
                    break
            elif choice == "3":
                print("Thank you for using the Cryptographer. Until next time!")
                done = True
            else:
                print("Wrong input. Please choose between numbers 1 to 3.")
        else:
            print("You haven't typed in anything! Please try again.")

main()
