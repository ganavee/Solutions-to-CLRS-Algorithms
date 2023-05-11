#Parameter way!
def sumNnumbersP(n, tot):
    if(n == 0):
        return tot
    tot += n
    return sumNnumbersP(n-1, tot)

#Function way
def sumNnumbersF(n):
    if(n == 0):
        return 0
    return n + sumNnumbersF(n-1)

n = int(input("Enter n: "))
print(f"Sum of first {n} numbers is {sumNnumbersP(n, 0)} using Parameter Way")
print(f"Sum of first {n} numbers is {sumNnumbersF(n)} using Function Way")
