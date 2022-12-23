#Sum of digits

def sumOfDigits(n, tot):
    if(n == 0):
        return tot
    return sumOfDigits(n // 10, tot + (n % 10))

print(sumOfDigits(430, 0))
