import sys

#Select Maximum/minimum element and put it into its right position

class Selection_sort:
    def sort_ascending(self, arr):
        sorting_index =len(arr)-1
        for j in range(len(arr)-1):
            largest_index = 0
            for i in range(1, sorting_index+1):
                if(arr[i] > arr[largest_index]):
                    largest_index = i
            if(sorting_index == largest_index):
                continue
            swap = arr[largest_index]
            arr[largest_index] = arr[sorting_index]
            arr[sorting_index] = swap
            sorting_index -= 1
            print(arr)
        print("Sorting using Selection sort: ", arr)



    
    def read_input(self):
        print("Enter Input Array")
        arr = sys.stdin.readline()
        arr = list(map(int, arr.strip().split()))
        print("Input Array is ", arr)
        self.sort_ascending(arr)

obj = Selection_sort()
obj.read_input()
