import sys

class Solution:
    def find(self, num):
        if(num == 0):
            xor = 0
        elif(num % 4 == 0):
            xor = num
        elif((num+1) % 4 == 0):
            xor = 0
        elif((num+2) % 4 == 0):
            xor = num+1
        elif((num+3) % 4 == 0):
            xor = 1
        else:
            xor = 0
        print("Xor of numbers from 0 to {0} is {1}".format(num, xor))

    
    def read_input(self):
        print("Enter Input number")
        num = int(sys.stdin.readline())
        print("Input num: {0}".format(num))
        self.find(num)

obj = Solution()
obj.read_input()
