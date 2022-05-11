def palindrome(n, count):
    if(n == 0):
        return 0
    return (n%10)*(10**count) + palindrome(n//10, count-1)


def second_approach(n, start, end):
    if(start > end):
        return True
    if(n[start] == n[end]):
        return second_approach(n, start+1, end-1)
    else:
        return False


num = 12321
count = 0
n = num
while(n!=0):
    n = n//10
    count += 1
return_num = palindrome(num, count-1)
if(num == return_num):
    print("The number {0} is a Palindrome".format(num))
else:
    print("The number {0} is not a Palindrome".format(num))

x = 1221
y = str(x)
z = [int(i) for i in y]
print("{0} Palindrome? {1}".format(x, second_approach(z, 0, len(z)-1)))
