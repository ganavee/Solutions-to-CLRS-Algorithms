#Find number of digits for any base
import sys
import math

class Solution:
    def find(self, num, base):
        digits = int(math.log(num, base)) + 1
        print("Number of digits in {0} base {1} is {2}".format(num, base, digits))
    
    def read_input(self):
        print("Enter Input number and base")
        arr = (sys.stdin.readline())
        arr = list(map(int, arr.strip().split()))
        num = arr[0]
        base = arr[1]
        print("Input num: {0} base: {1}".format(num, base))
        self.find(num, base)

obj = Solution()
obj.read_input()
