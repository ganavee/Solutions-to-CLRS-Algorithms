#Sum n to 1
def total(n, tot):
    if(n == 0):
        return tot
    return total(n-1, n + tot)

print(total(5, 0))
