
from FileIO import readFile, writeFile, loadAndSaveImageFromWeb
from Statistics import addToStats, doStatistics
import sys
from Encrypt import EncryptClass

encryptObject = EncryptClass()

def main():
    print("+---------------------------------------+")
    print("|Welcome to the AM Steganography Service|")
    print("|Please follow the instructions as they |")
    print("|appear.                                |")
    print("|When prompted for input, you can always|")
    print("|exit the program by pressing [E] ...   |")
    print("+---------------------------------------+")
    #time.sleep(1)
    encryptOrDecrypt()


def encryptOrDecrypt():
    choice = input("Do you wish to\n(1)Encrypt\n(2)Decrypt\n(3)Add image to collection\nor\n(4)Run Statistics\nInput: ")

    # Encryption
    if choice == '1':
        writeInputOrReadFromFile(True)
        choice = input("Do you wish to perform further operations? (Y/N): ")
        if choice == 'y' or choice == 'Y':
            encryptOrDecrypt()
        else:
            sys.exit()

    # Decryption
    elif choice == '2':
        writeInputOrReadFromFile(False)
        choice = input("Do you wish to perform further operations? (Y/N): ")
        if choice == 'y' or choice == 'Y':
            encryptOrDecrypt()
        else:
            sys.exit()

    elif choice == '3':
        loadAndSaveImageFromWeb()
        choice = input("Do you wish to perform further operations? (Y/N): ")
        if choice == 'y' or choice == 'Y':
            encryptOrDecrypt()
        else:
            sys.exit()

    elif choice == '4':
        doStatistics()
        choice = input("Do you wish to perform further operations? (Y/N): ")
        if choice == 'y' or choice == 'Y':
            encryptOrDecrypt()
        else:
            sys.exit()

    elif choice == 'e' or choice == 'E':
        sys.exit()

    else:
        print("Invalid input. Please press [1] OR [2] to choose a function:")
        encryptOrDecrypt()


def writeInputOrReadFromFile(encrypt):
    choice = input("Do you wish to\n(1)Write the message\nor\n(2)Read from file\nInput: ")

    if encrypt:
        # Input message
        if choice == '1':
            text = input("Please input your message\n")
            text = text.lower()
            result = encryptObject.encryptMessage(text)
            print("Your encrypted string: " + result)
            addToStats(text)
            writeToFile(result)

        # Read file
        elif choice == '2':
            text = readFile()
            text = text.lower()
            result = encryptObject.encryptMessage(text)
            print("Your encrypted string: " + result)
            addToStats(text)
            writeToFile(result)

        elif choice == 'e' or choice == 'E':
            sys.exit()

        else:
            print("Invalid input. Please press [1] OR [2] to choose a function:")
            writeInputOrReadFromFile(encrypt)

    else:
        # Input message
        if choice == '1':
            text = input("Please input your message\n")
            result = encryptObject.decryptMessage(text)
            print("Your decrypted string: ", result)
            writeToFile(result)

        # Read file
        elif choice == '2':
            text = readFile()
            result = encryptObject.decryptMessage(text)
            print("Your decrypted string: " + result)
            writeToFile(result)

        elif choice == 'e' or choice == 'E':
            sys.exit()

        else:
            print("Invalid input. Please press [1] OR [2] to choose a function:")
            writeInputOrReadFromFile(encrypt)


def writeToFile(result):
    choice = input("Do you wish to save to a file? (Y/N)")
    if choice == 'y' or choice == 'Y':
        writeFile(result)

    elif choice == 'n' or choice == 'N':
        pass

    elif choice == 'e' or choice == 'E':
        sys.exit()

    else:
        writeToFile()




if __name__ == '__main__':
    main()