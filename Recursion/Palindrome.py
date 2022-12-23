#Palindrome

def reverse(n, rev):
    if(n == 0):
        return rev
    return reverse(n // 10, (rev * 10) + (n % 10))

n = 676
rev = reverse(n, 0)
if(n == rev):
    print("The given number is a palindrome")
else:
    print("The given number is not a palindrome")
