import sys
import math

class Prime:
    def find(self, num):
        if(num < 1):
            print("{0} is not prime".format(num))
            return
        for i in range(2, num):
            if(num%i == 0):
                print("{0} is not prime".format(num))
                return
        print("{0} is prime".format(num))

    def square_root(self, num):
        if(num < 1):
            print("{0} is not prime".format(num))
            return
        for i in range(2, int(math.sqrt(num))+1):
            if(num%i == 0):
                print("{0} is not prime".format(num))
                return
        print("{0} is prime".format(num))


    def read_input(self):
        print("Enter Number")
        num = int(sys.stdin.readline())
        print("Input Number:", num)
        self.square_root(num)

obj = Prime()
obj.read_input()
