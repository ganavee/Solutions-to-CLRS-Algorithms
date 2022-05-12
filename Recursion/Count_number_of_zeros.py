def count(n, tot):
    if(n == 0):
        return tot
    if(n%10 == 0):
        tot += 1
    return count(n//10, tot)
    pass

num = 2050060
print("Number of zeros in {0} is {1}".format(num, count(num, 0)))
