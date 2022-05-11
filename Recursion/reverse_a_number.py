def reverse_a_number_using_str(n):
    if(n == 0):
        return ""
    return str(n%10) + reverse_a_number_using_str(n//10)

def reverse_second_approach(n):
    if(n == 0):
        return 0
    #count number of digits
    num = n
    count = 0
    while(num!=0):
        num = num//10
        count += 1
    return (n%10)*(10**(count-1)) + reverse_second_approach(n//10)

def reverse_third_approach(n, count):
    if(n == 0):
        return 0
    return (n%10)*(10**(count)) + reverse_third_approach(n//10, count-1)



num = 12456
count = 0
n = num
while(n!=0):
    n = n//10
    count += 1

if(reverse_a_number_using_str(num)==""):
    print("Reverse of the number {0} is {1}".format(num, 0))
else:
    print("Reverse of the number {0} is {1}".format(num, reverse_a_number_using_str(num)))

print("Reverse of the number {0} is {1}".format(num, reverse_second_approach(num)))
print("Reverse of the number {0} is {1}".format(num, reverse_third_approach(num, count-1)))

