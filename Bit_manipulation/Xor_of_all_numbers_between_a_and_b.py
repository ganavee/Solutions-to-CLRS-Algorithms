import sys

class Solution:
    def find(self, a, b):
        print("xor of {0} is {1} ".format(a, self.find_xor(a)))
        print("xor of {0} is {1} ".format(b, self.find_xor(b)))
        final = self.find_xor(a-1) ^ self.find_xor(b)
        print("Final ", abs(final))

    def find_xor(self, num):
        if(num % 4 == 0):
            xor = num
        elif(num % 4  == 1):
            xor = 1
        elif(num % 4  == 2):
            xor = num+1
        elif(num % 4  == 3):
            xor = 0
        else:
            xor = 0
        return xor

    
    def read_input(self):
        print("Enter Input number")
        arr = (sys.stdin.readline())
        arr = list(map(int, arr.strip().split()))
        a = arr[0]
        b = arr[1]
        print("Input nums: {0}, {1}".format(a, b))
        self.find(a, b)

obj = Solution()
obj.read_input()
