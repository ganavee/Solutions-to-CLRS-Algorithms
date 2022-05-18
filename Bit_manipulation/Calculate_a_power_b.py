 
import sys
import math

class Solution:
    def find(self, base, power):
        p = power
        ans = base
        while(power != 0):
            if(power & 1 == 1):
                ans *= base
            power = power >> 1
        print("{0} power {1} is {2}".format(base, p, ans))
    
    def read_input(self):
        print("Enter base and power")
        arr = (sys.stdin.readline())
        arr = list(map(int, arr.strip().split()))
        base, power = arr[0:]
        print("Base: {0} Power {1}".format(base, power))
        self.find(base, power)

obj = Solution()
obj.read_input()
