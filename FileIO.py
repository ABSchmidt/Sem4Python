import os
from PIL import Image
import requests
from io import BytesIO


def readFile():
    userinput = input('Enter filepath: ')

    fromFile = ''
    eof = False
    file = open(userinput)
    while eof == False:
        data = file.readline()
        #data.rstrip('\n')
        fromFile += data
        if data == '':
            file.close()
            eof = True

    print(fromFile)
    return fromFile


#mangler file-chooser
def writeFile(message):
    filename = input("Please input a filename (no extensions): ")
    basePath = os.getcwd()
    completePath = os.path.join(basePath, filename + ".txt")
    file = open(completePath, "w")
    file.write(message)
    file.close()
    print("Your message has been saved here: " + completePath)


def loadAndSaveImageFromWeb():
    url = input("Please input the image url: ")
    name = input("Please give the image a name - no extensions: ")
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    filename = name + ".png"
    path = os.path.join(os.getcwd(), filename)
    img.save(path)
    with open("imagefilenames.txt", "a") as file:
        file.write(filename + "\n")


#loadAndSaveImageFromWeb("https://www.rd.com/wp-content/uploads/2018/01/Burano_Amazing-Photos-of-Towns-with-Colorful-Houses-Around-the-World.jpg","colorful_houses")