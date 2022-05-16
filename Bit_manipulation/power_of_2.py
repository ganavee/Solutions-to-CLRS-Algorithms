#Find number of digits for any base
import sys
import math

class Solution:
    def find(self, num):
        count = 0
        n = num
        while(num != 0):
            if(num & 1):
                count += 1
            num = num >> 1
        if(count == 1):
            print("{0} is power of 2".format(n))
        else:
            print("{0} is not power of 2".format(n))

    def method_2(self, num):
        if(num == 0):
            print("{0} is not power of 2".format(num))
            return
        if(num & (num-1) == 0):
            print("{0} is power of 2".format(num))
        else:
            print("{0} is not power of 2".format(num))
    
    def read_input(self):
        print("Enter Input number")
        num = int(sys.stdin.readline())
        print("Input num: {0}".format(num))
        #self.find(num)
        self.method_2(num)

obj = Solution()
obj.read_input()
