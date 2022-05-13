import sys

class Insertion_sort:
    def sort_iter_asc_3loops(self, arr):
        i = 1
        for i in range(1, len(arr)):
            for j in range(0,i):
                if(arr[j] > arr[i]):
                    val = arr[i]
                    for k in range(i-1,j-1, -1):
                        arr[k+1] = arr[k]
                    arr[j] = val
        print("Sorting using Insertion Sort: ", arr)

    def sort_asc_iter_2loops(self, arr):
        for i in range(0, len(arr)-1):
            for j in range(i+1, 0, -1):
                if(arr[j-1] > arr[j]):
                    temp = arr[j]
                    arr[j] = arr[j-1]
                    arr[j-1] = temp
                else:
                    break
        print("Sorting using Insertion Sort using 2 loops: ", arr)
        pass
    
    def read_input(self):
        print("Enter Input Array")
        arr = sys.stdin.readline()
        arr = list(map(int, arr.strip().split()))
        print("Input Array is ", arr)
        #self.sort_iter_asc_3loops(arr)
        self.sort_asc_iter_2loops(arr)

obj = Insertion_sort()
obj.read_input()
