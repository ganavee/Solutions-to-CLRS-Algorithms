import sys

class Solution:
    def reset_ith_bit(self, num, ith_bit):
        n = num
        mask = 1 << (ith_bit-1)
        num ^= mask
        print("{0} after setting {1}th bit is {2}".format(n, ith_bit, num))
    
    def read_input(self):
        print("Enter inputs")
        arr = sys.stdin.readline()
        arr = list(map(int, arr.strip().split()))
        num = arr[0]
        ith_bit = arr[1]
        print("Input num: {0} ith_bit: {1}".format(arr, ith_bit))
        self.reset_ith_bit(num, ith_bit)

obj = Solution()
obj.read_input()
