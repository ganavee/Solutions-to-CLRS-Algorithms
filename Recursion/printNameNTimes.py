#Time Complexity:  O(n)
#Space Complexity: O(n)
def printFun(i):
    if(i == 0):
        return
    print("Ganavi got Job Offer")
    printFun(i-1)

n = int(input("Enter the number of times you want to print the sentence: "))
printFun(n)

