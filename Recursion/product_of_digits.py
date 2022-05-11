def product_of_digits(n):
    if(n == 0):
        return 1
    return (n%10)*product_of_digits(n//10)

num = 352
print("Product of digits {0} is {1}".format(num, product_of_digits(num)))
