def sum_of_digits(n):
    if(n == 0):
        return 0
    return (n%10) + sum_of_digits(n//10)

num = 1342
print("Sum of the digits of num {0} is {1}".format(num, sum_of_digits(num)))
