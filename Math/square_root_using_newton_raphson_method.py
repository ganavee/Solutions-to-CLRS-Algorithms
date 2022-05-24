import sys
import math

class SquareRoot:
    def sqrt(self, num):
        x = num
        while(True):
            root = 0.5*(x + (num/x))
            if(abs(root-x) < 0.5):
                return root
            x = root
    
    def read_input(self):
        print("Enter Number")
        num = int(sys.stdin.readline())
        print("Input Number: {0}".format(num))
        x = self.sqrt(num)
        print("Square root of {0} is {1} ".format(num, x))

obj = SquareRoot()
obj.read_input()
