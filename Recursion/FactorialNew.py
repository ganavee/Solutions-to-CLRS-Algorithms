#TC O(n)
#SC O(N)
def factP(n):
    if(n == 1):
        return 1
    return n * factP(n-1)

#TC O(n)
#SC O(1)
def factF(n, f):
    if(n == 1):
        return f
    return factF(n-1, n*f)

n = int(input("Enter n: "))
print(f"Factorial of {n} using Parameter Way is {factP(n)}")
print(f"Factorial of {n} using Functional Way is {factF(n, 1)}")
