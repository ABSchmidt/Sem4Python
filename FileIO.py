import os.path

def readFile():
    userinput = input('Enter filepath: ')

    fromFile = ''
    eof = False
    file = open(userinput)
    while(eof == False):
        data = file.readline()
        #data.rstrip('\n')
        fromFile += data
        if(data == ''):
            file.close()
            eof = True

    print(fromFile)
    return fromFile


#mangler file-chooser
def writeFile(message):
    filename = input("Please input a filename (no extensions): ")
    basePath = "C:/Users/admin/Documents/"
    completePath = os.path.join(basePath, filename + ".txt")
    file = open(completePath, "w")
    file.write(message)
    file.close()
    print("Your message has been saved here: " + completePath)

#writeFile("badabing", "badaboom")
