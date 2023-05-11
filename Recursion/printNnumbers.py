#Time Complexity:  O(n)
#Space Complexity: O(n)

#Backtracking
def print1toNBT(n):
    if(n == 0):
        return
    print1toNBT(n-1)
    print(n)

#Backtracking
def printNto1BT(i, n):
    if(i > n):
        return
    printNto1BT(i+1, n)
    print(i)

#Recursion
def print1toN(i, n):
    if(i > n):
        return
    print(i)
    print1toN(i+1, n)

#Recursion
def printNto1(n):
    if(n == 0):
        return
    print(n)
    printNto1(n-1)
    
n = int(input("Enter n: "))
print(f"Printing 1 to {n} using Recursion")
print1toN(1, n)
print(f"Printing {n} to 1 using Recursion")
printNto1(n)
print(f"Printing 1 to {n} using BackTracking")
print1toNBT(n)
print(f"Printing {n} to 1 using BackTracking")
printNto1BT(1, n)
