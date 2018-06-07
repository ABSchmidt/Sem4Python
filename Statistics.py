def addToStats(text):
    file = open("allStrings.txt", 'a')
    file.write(text + "\n")
    file.close()

def readStrings():
    with open("allStrings.txt") as file:
        lines = file.readlines()

    return lines

def calcAvgLen(messages):
    numberOfMsgs = len(messages)
    print("number of msgs: " + str(numberOfMsgs))
    totalMsgLen = 0

    for j in range (0, numberOfMsgs):
        oneMsg = messages[j]
        oneMsg = oneMsg.strip(' \t\n\r')
        print("length of msg: " + str(len(oneMsg)))
        totalMsgLen += len(messages[j])

    return totalMsgLen/numberOfMsgs


alphabet = {
    'a':0, 'b':0, 'c':0, 'd':0,
    'e':0, 'f':0, 'g':0, 'h':0,
    'i':0, 'j':0, 'k':0, 'l':0,
    'm':0, 'n':0, 'o':0, 'p':0,
    'q':0, 'r':0, 's':0, 't':0,
    'u':0, 'v':0, 'w':0, 'x':0,
    'y':0, 'z':0
}

def calcUsePctOfLetters(messages):

    #Count instances of letters
    for k in range(0, len(messages)):

        singleMsg = messages[k]
        for l in range(0, len(singleMsg)):
            aChar = singleMsg[l]
            aChar = aChar.strip(' \t\n\r')
            if(aChar.isalpha()):
                alphabet[aChar] = alphabet[aChar] + 1
                #print(aChar + ": " + str(alphabet[aChar]))
            else:
                pass

    #Calculate total number of letters
    totalCount = 0
    for letter in alphabet:
        totalCount += alphabet[letter]

    #Calculate percentages
    for letter in alphabet:
        percentage = alphabet[letter]/totalCount*100
        print("Percentage of " + letter + ": " + str(percentage))


def doStatistics():
    messages = readStrings()
    #avgLenOfMsg = calcAvgLen(messages)
    calcUsePctOfLetters(messages)
