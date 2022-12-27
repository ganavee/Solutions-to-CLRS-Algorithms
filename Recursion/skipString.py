#Skip a string

def skip(originalStr, string):
    if(len(originalStr) < len(string)):
        return originalStr
    startIndex = 0
    lenString = len(string)
    endIndex = lenString - 1
    subStart = -1
    subEnd = -1
    resStr = ""
    i = 0
    noSub = True
    orgStart = 0
    while(i < len(originalStr)):
        if(startIndex == 0):
            subStart = i
        if(startIndex <= endIndex):
            if(originalStr[i] == string[startIndex]):
                startIndex += 1
            else:
                if(startIndex != 0):
                    i -= 1
                startIndex = 0
                

        if(startIndex == lenString):
            noSub = False
            subEnd = i
            #remove that string
            resStr = resStr + originalStr[orgStart:subStart] 
            orgStart = i+1
            startIndex = 0
            
        i += 1
    if(orgStart != len(originalStr)):
        resStr = resStr + (originalStr[orgStart:])
    if(noSub == True):
        print("String = ", originalStr)
    else:
        print("String = ", resStr)


originalStr = "ganaviisthebestbestestprogrammerbestesthello"
string = "bestest"
skip(originalStr, string)
