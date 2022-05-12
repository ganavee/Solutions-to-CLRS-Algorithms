import sys

class linear_search:
    def search_single(self, arr, n, start):
        if(start == len(arr)):
            return False
        if(arr[start] == n):
            return True
        return self.search_single(arr, n, start+1)
        

    def search_mutiple(self, arr, target, start, target_indices):
        if(start == len(arr)):
            return target_indices
        if(arr[start] == target):
            target_indices.append(start)
        return self.search_mutiple(arr, target, start+1, target_indices)
    
    def search_mutiple_noextraspace(self, arr, target, start):
        target_indices = []
        if(start == len(arr)):
            return target_indices
        if(arr[start] == target):
            target_indices.append(start)
        returned = self.search_mutiple_noextraspace(arr, target, start+1)
        #print(" start {0} returned {1} target_indicies {2}".format(start, returned, target_indices))
        target_indices.extend(returned)
        #print("After appending ", target_indices)
        return target_indices

    def read_input(self):
        arr = sys.stdin.readline()
        arr = list(map(int, arr.strip().split()))
        search_elem = arr[-1]
        arr = arr[:len(arr)-1]
        #To search for single occurences
        print("Input Array {0} Search element {1}".format(arr, search_elem))
        print("Element {0} present? {1}".format(search_elem, self.search_single(arr, search_elem, 0)))
        #To search for multiple occurences
        target_indices = []
        target_indices = self.search_mutiple(arr, search_elem, 0, target_indices)
        print("METHOD 1: The list of indices of the target element {0} is {1}".format(search_elem, target_indices))
        target_indices_noextraspace = self.search_mutiple_noextraspace(arr, search_elem, 0)
        print("METHOD 2: The list of indices of the target element {0} is {1}".format(search_elem, target_indices_noextraspace))


obj = linear_search()
obj.read_input()
 
