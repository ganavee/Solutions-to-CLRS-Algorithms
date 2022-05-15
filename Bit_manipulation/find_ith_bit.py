import sys

class Solution:
    def find(self, num, ith_bit):
        n = num
        num = num >> (ith_bit-1)
        print("{0}th bit of {1} is {2}".format(ith_bit, n, (num & 1)))
        
    
    def read_input(self):
        print("Enter inputs")
        arr = sys.stdin.readline()
        arr = list(map(int, arr.strip().split()))
        num = arr[0]
        ith_bit = arr[1]
        print("Input num: {0} ith_bit: {1}".format(arr, ith_bit))
        self.find(num, ith_bit)

obj = Solution()
obj.read_input()
