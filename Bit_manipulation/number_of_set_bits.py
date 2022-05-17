 
import sys
import math

class Solution:
    def find(self, num):
        n = num
        count = 0
        while(num):
            if(num & 1):
                count += 1
            num >>= 1
        print("Number of set bits in {0} is {1}".format(n, count))
       
    
    def read_input(self):
        print("Enter number")
        num = int(sys.stdin.readline())
        print("Number: {0}".format(num))
        self.find(num)

obj = Solution()
obj.read_input()
