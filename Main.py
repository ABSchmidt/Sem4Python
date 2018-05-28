from PIL import Image
from FileIO import readFile, writeFile
import sys
import time

im = Image.open('Nature01_lake.png')
image = im.load()

def locateValueInPic(inputValue):
    found = False
    pixelPos = 0
    for y in range(1,100):

        for x in range(1,100):
            rgbValues = image[x,y]

            for i in range(0,3) :
                singleValue = rgbValues[i]
                if singleValue == inputValue:
                    found = True
                    pixelPos = i

                if(found):
                    break
            if(found):
                break
        if(found):
            break
    return str(x)+'-'+str(y)+'-'+str(pixelPos)

def locateCharInPic(x, y, rgb):
    aPixel = image[x,y]
    charVal = aPixel[rgb]
    return chr(charVal)


def decryptMessage(encryptedmsg):
    plainString = ''

    listOfWords = encryptedmsg.split('*')
    if(len(listOfWords[len(listOfWords)-1]) < 1):
        listOfWords.pop(len(listOfWords)-1)

    for o in range(0, len(listOfWords)):

        listOfLetters = listOfWords[o].split('!')
        if(len(listOfLetters[len(listOfLetters)-1]) < 1):
            listOfLetters.pop(len(listOfLetters)-1)

        #print(str(listOfLetters))
        for m in range(0, len(listOfLetters)):
            seperateVals = listOfLetters[m].split('-')
            #print(str(seperateVals))
            plainString += str(locateCharInPic(int(seperateVals[0]),int(seperateVals[1]),int(seperateVals[2])))
        plainString += ' '
    print(plainString)



def encryptMessage(text):
    #print("Method: processInput")

    #listOfLocations er en string af location-strings, det vil sige den egentlige "hash"-kode
    listOfLocations = ""

    listOfWords = text.split()
    for k in range(0, len(listOfWords)):

        listOfLetters = (listOfWords[k])
        for j in range(0,len(listOfLetters)):
            #location er en string med x-koordinat, y-koordinat og r/g/b-angiver for en char's position i billedfilen
            location = locateValueInPic(ord(listOfLetters[j]))
            listOfLocations += location + "!"
        listOfLocations += "*"
    return listOfLocations
    print("Encrypted String: " + listOfLocations)

def encryptOrDecrypt():
    choice = input("Do you wish to\n(1)Encrypt\nor\n(2)Decrypt\nInput: ")

    # Encryption
    if (choice == '1'):
        writeInputOrReadFromFile(True)

    # Decryption
    elif (choice == '2'):
      writeInputOrReadFromFile(False)

    elif (choice == 'e' or choice == 'E'):
        sys.exit()

    else:
        print("Invalid input. Please press [1] OR [2] to choose a function:")
        encryptOrDecrypt()


def writeInputOrReadFromFile(encrypt):
    choice = input("Do you wish to\n(1)Write the message\nor\n(2)Read from file\nInput: ")

    # Input message
    if (choice == '1'):
        text = input("Please input your message\n")
        result = encryptMessage(text)
        print("Your encrypted string: " + result)
        writeToFile(result)

    # Read file
    elif (choice == '2'):
        text = readFile()
        result = encryptMessage(text)
        print("Your encrypted string: " + result)
        writeToFile(result)

    elif (choice == 'e' or choice == 'E'):
        sys.exit()

    else:
        print("Invalid input. Please press [1] OR [2] to choose a function:")
        writeInputOrReadFromFile(encrypt)


def writeToFile(result):
    choice = input("Do you wish to save to a file? (Y/N)")
    if (choice == 'y' or choice == 'Y'):
        writeFile(result)

    elif (choice == 'n' or choice == 'N'):
        sys.exit()

    elif (choice == 'e' or choice == 'E'):
        sys.exit()

    else:
        writeToFile()

def main():
    print("+---------------------------------------+")
    print("|Welcome to the AM Steganography Service|")
    print("|Please follow the instructions as they |")
    print("|appear.                                |")
    print("|When prompted for input, you can always|")
    print("|exit the program by pressing [E] ...   |")
    print("+---------------------------------------+")
    time.sleep(2)
    encryptOrDecrypt()


if __name__ == '__main__':
    main()