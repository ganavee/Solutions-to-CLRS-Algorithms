import sys

class Ceiling:
    def find(self, arr, target):
        start = 0
        end = len(arr) - 1
        mid = 0
        while(start <= end):
            mid = start + (end - start)//2
            if(arr[mid] < target):
                start = mid + 1
            elif(arr[mid] > target):
                end = mid - 1
            else:
                print("Ceiling of {0} is {1}".format(target, arr[mid]))
                return
        print("Ceiling of {0} is {1}".format(target, arr[start]))
        '''
        #another approach
        if(arr[mid] < target):
            print("Ceiling of {0} is {1}".format(target, arr[mid+1]))
            #break
            mid -= 1
        else:
             print("Ceiling of {0} is {1}".format(target, arr[mid]))
        '''
    
    def input(self):
        print("Enter sorted array")
        arr = list(map(int, sys.stdin.readline().strip().split()))
        print("Enter the target")
        target = int(sys.stdin.readline())
        print("Array is {0} Target is {1}".format(arr, target))
        self.find(arr, target)

obj = Ceiling()
obj.input()
