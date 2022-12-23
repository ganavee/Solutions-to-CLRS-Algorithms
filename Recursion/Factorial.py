#Factorial Of a number

def fac(n, prod):
    if(n == 0):
        return prod
    return fac(n - 1, prod * n)
0
print(fac(4, 1))
