import sys

def odd_even():
    print("Enter a number")
    num = int(sys.stdin.readline())
    print("Input: ", num)
    if((num & 1)==0):
        print("{0} is even".format(num))
    else:
        print("{0} is odd".format(num))

        
odd_even()
