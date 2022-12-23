#Reverse a number

def reverse(n, rev):
    if(n == 0):
        return rev
    return reverse(n // 10, (rev * 10) + (n % 10))

print(reverse(670, 0))
