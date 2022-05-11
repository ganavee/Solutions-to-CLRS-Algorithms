def sum_n_to_1(n):
    if(n == 1):
        return 1
    return n + sum_n_to_1(n-1)
    pass

num = 9
print("Sum of numbers from {0} to 1 is {1}".format(num, sum_n_to_1(num)))
