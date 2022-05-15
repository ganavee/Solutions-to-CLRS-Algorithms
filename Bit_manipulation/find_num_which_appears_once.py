import sys

class Solution:
    def find(self, arr):
        xor = arr[0]
        for i in range(1, len(arr)):
            xor ^= arr[i]
        print("The number which appears only once is {0} is {1}".format(arr, xor))
        
    
    def read_input(self):
        print("Enter input array")
        arr = sys.stdin.readline()
        arr = list(map(int, arr.strip().split()))
        print("Input array: ", arr)
        self.find(arr)

obj = Solution()
obj.read_input()
