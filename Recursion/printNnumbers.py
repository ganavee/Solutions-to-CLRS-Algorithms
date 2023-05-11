#Time Complexity:  O(n)
#Space Complexity: O(n)
def print1toN(n):
    if(n == 0):
        return
    print1toN(n-1)
    print(n)

def printNto1(n):
    if(n == 0):
        return
    print(n)
    printNto1(n-1)
    
n = int(input("Enter n: "))
print(f"Printing 1 to {n}")
print1toN(5)
print(f"Printing {n} to 1")
printNto1(5)
