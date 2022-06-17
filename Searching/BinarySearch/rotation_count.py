import sys

class Search:
    def proc(self, arr):
        start = 0
        end = len(arr)-1
        while(True):
            mid = start + (end-start)//2
            if(arr[mid]>arr[mid+1]):
                print("Array is roated {0} times".format(mid+1))
                break
            elif(arr[start]>arr[mid]):
                #1st part uneven
                end = mid
                #2nd part ascending
            else:
                #1st part ascending
                #2nd part uneven
                start = mid+1
               
    
    def input(self):
        print("Enter array")
        arr = list(map(int, sys.stdin.readline().strip().split()))
        print("Array is ", arr)
        self.proc(arr)

obj = Search()
obj.input()
