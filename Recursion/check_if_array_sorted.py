import sys
class check_sorted:

    def check_sorted(self, arr, prev):
        if(prev == (len(arr)-1)):
            return True
        if(arr[prev] < arr[prev+1]):
            return self.check_sorted(arr, prev+1)
        else:
            return False

    def read_input(self):
        arr = sys.stdin.readline()
        arr = list(map(int, arr.strip().split()))
        print("Input Array ", arr)
        print("Array is sorted? ",self.check_sorted(arr, 0))


obj = check_sorted()
obj.read_input()

