#Product of digits

def productOfDigits(n, tot):
    if(n == 0):
        return tot
    return productOfDigits(n // 10, tot * (n % 10))

print(productOfDigits(567, 1))
