from PIL import Image

im = Image.open('Nature01_lake.png')
image = im.load()

def locateValueInPic(inputValue):
    found = False
    pixelPos = 0
    for y in range(1,100):

        for x in range(1,100):
            rgbValues = image[x,y]
            #rgbValues = [rgbValuesTuple]

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

    listOfLetters = encryptedmsg.split('!')
    #print(str(listOfLetters))
    for m in range(0, len(listOfLetters)):
        seperateVals = listOfLetters[m].split('-')
        #print(str(seperateVals))
        plainString += str(locateCharInPic(int(seperateVals[0]),int(seperateVals[1]),int(seperateVals[2])))
    print(plainString)



def encryptMessage(text):
    #print("Method: processInput")

    #listOfLocations er en string af location-strings, det vil sige den egentlige "hash"-kode
    listOfLocations = ""

    listOfWords = text.split()
    for k in range(0, len(listOfWords)):

        listOfLetters = (listOfWords[k])
        print(str(listOfLetters))
        for j in range(0,len(listOfLetters)):
            #location er en string med x-koordinat, y-koordinat og r/g/b-angiver for en char's position i billedfilen
            location = locateValueInPic(ord(listOfLetters[j]))
            listOfLocations += location + "!"
            #print("send me your location: " + str(location))

    listOfLocations = listOfLocations[:-1]
    print("listOfLocations: " + listOfLocations)

def main():
    choice = int(input("Do you wish to\n(1)Encrypt\nor\n(2)Decrypt\nInput: "))
    if (choice == 1):
        text = input("Please input your message\n")
        encryptMessage(text)
    elif (choice == 2):
        text = input("Please input your encrypted message\n")
        decryptMessage(text)
    else:
        print("Invalid input. Please press [1] OR [2] to choose a function:")
        main()


if __name__ == '__main__':
    main()