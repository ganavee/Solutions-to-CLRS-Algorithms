import sys

class BinarySearch:
    def search(self, arr, target):
        start = 0
        end = 0
        power = 1
        while(not(target >= arr[start] and target <= arr[end])):
            start = end + 1
            end += 2**power
            print("start = {0} end = {1}".format(start, end))
            power += 1
        while(start <= end):
            mid = start + (end-start)//2
            if(target < arr[mid]):
                end = mid - 1
            elif(target > arr[mid]):
                start = mid + 1
            else:
                print("Element {0} found at {1}".format(target, mid))
                return
        print("Element {0} not found".format(target))
            

    
    def input(self):
        print("Enter the array")
        arr = list(map(int, sys.stdin.readline().strip().split()))
        print("Enter the target")
        target = int(sys.stdin.readline().strip())
        print("Array = {0} target = {1}".format(arr, target))
        self.search(arr, target)


obj = BinarySearch()
obj.input()
