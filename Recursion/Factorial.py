def factorial(n):
    if(n == 1):
        return 1
    return n*factorial(n-1)


num = 4
print("Factorial of {0} is {1}".format(num, factorial(num)))
