import sys

class Bubble_sort:
    def sort(self, arr):
        for i in range(len(arr)-1,0, -1):
            swapped = False
            for j in range(i):
                if(arr[j] > arr[j+1]):
                    swapped = True
                    swap = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = swap
            if(swapped == False):
                print("Already swapped")
                break
        print("Sorting using Bubble sort : ", arr)
    
    def read_input(self):
        print("Enter Input Array")
        arr = sys.stdin.readline()
        arr = list(map(int, arr.strip().split()))
        print("Input Array is ", arr)
        self.sort(arr)

obj = Bubble_sort()
obj.read_input()
