#Print n to 1

def printNumberRev(n):
    if(n == 0):
        return
    print(n)
    printNumberRev(n-1)

#printNumberRev(5)


#Print 1 to n
def printNumber(n):
    if(n == 0):
        return
    printNumber(n-1)
    print(n)

printNumber(5)
