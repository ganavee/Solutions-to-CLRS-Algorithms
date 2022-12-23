#To print first 5 numbers


def recursion(n, maxNum):
    if(n == maxNum+1):
        return
    print(n)
    return recursion(n + 1, maxNum)

recursion(1, 10)
