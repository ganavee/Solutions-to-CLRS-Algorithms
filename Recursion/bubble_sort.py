import sys
class Bubble_sort:
    def sort(self, arr, r, c):
        if(c == 1):
            return 
        if(r < c-1):
            if(arr[r] > arr[r+1]):
                swap = arr[r]
                arr[r] = arr[r+1]
                arr[r+1] = swap
            self.sort(arr, r+1, c)
        else:
            self.sort(arr, 0, c-1)

    
    def input(self):
        print("Enter the array")
        arr = sys.stdin.readline()
        arr = list(map(int, arr.strip().split()))
        print("Input Array is ", arr)
        self.sort(arr, 0, len(arr))
        print("Sorted array is ", arr)


obj = Bubble_sort()
obj.input()
