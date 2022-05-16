#Find nth magic number(Refer Anki for magic number or refer Kunal's bitwise operators)
import sys

class Solution:
    def find(self, num):
        count = 1
        n = num
        magic = 0
        while(num != 0):
            magic += (num & 1)*(5**count)
            count += 1
            num = num >> 1
        print("{0}th magic number is {1}".format(n, magic))

    
    def read_input(self):
        print("Enter Input number")
        num = int(sys.stdin.readline())
        print("Input num: {0}".format(num))
        self.find(num)

obj = Solution()
obj.read_input()
