from PIL import Image


class EncryptClass:

    listOfImages = []


    def loadListOfImages(self):
        global listOfImages
        with open("imagefilenames.txt") as file:
            listOfImages = file.readlines()

        for x in range(0,len(listOfImages)):
            listOfImages[x] = listOfImages[x].rstrip()


    def loadImage(self):
        global listOfImages
        imgChoice = int(input("Please choose a picture by inputting a number between %d and %d: " % (1,len(listOfImages))))
        global im
        im = Image.open(listOfImages[imgChoice-1])
        global image
        image = im.load()


    def locateValueInPic(self,inputValue):
        found = False
        pixelPos = 0
        for y in range(1, 100):

            for x in range(1, 100):
                rgbValues = image[x,y]

                for i in range(0, 3):
                    singleValue = rgbValues[i]
                    if singleValue == inputValue:
                        found = True
                        pixelPos = i
                        break
                if found:
                    break
            if found:
                break
        return str(x)+'-'+str(y)+'-'+str(pixelPos)


    def locateCharInPic(self, x, y, rgb):
        aPixel = image[x, y]
        charVal = aPixel[rgb]
        return chr(charVal)


    def decryptMessage(self, encryptedmsg):
        self.loadListOfImages()
        self.loadImage()

        plainString = ''

        listOfWords = encryptedmsg.split('*')
        if len(listOfWords[len(listOfWords)-1]) < 1:
            listOfWords.pop(len(listOfWords)-1)

        for o in range(0, len(listOfWords)):

            listOfLetters = listOfWords[o].split('!')
            if len(listOfLetters[len(listOfLetters)-1]) < 1:
                listOfLetters.pop(len(listOfLetters)-1)

            for m in range(0, len(listOfLetters)):
                seperateVals = listOfLetters[m].split('-')
                plainString += str(self.locateCharInPic(int(seperateVals[0]),int(seperateVals[1]),int(seperateVals[2])))
            plainString += ' '
        return plainString


    def encryptMessage(self, text):
        self.loadListOfImages()
        self.loadImage()

        #listOfLocations er en string sammensat af location-strings, det vil sige den egentlige "hash"-kode
        listOfLocations = ""

        listOfWords = text.split()
        for k in range(0, len(listOfWords)):

            listOfLetters = (listOfWords[k])
            for j in range(0,len(listOfLetters)):

                #location er en string med x-koordinat, y-koordinat og r/g/b-angiver for en char's position i billedfilen
                location = self.locateValueInPic(ord(listOfLetters[j]))
                listOfLocations += location + "!"
            listOfLocations += "*"
        return listOfLocations

