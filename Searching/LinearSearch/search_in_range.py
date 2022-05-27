import sys
class Search_in_range:
    def search(self, arr, target, start, end):
        for i in range(start, end+1):
            if(target == arr[i]):
                return True
        return False
    
    def input(self):
        print("Enter the Array")
        arr = list(map(int, sys.stdin.readline().strip().split()))
        print("Enter number to be searched")
        target = int(sys.stdin.readline())
        print("Enter the Range")
        start, end = list(map(int, sys.stdin.readline().strip().split()))
        print("Input arr = {0} and target is {1} start = {2} end = {3}".format(arr, target, start, end))
        print("Is {0} present in {1} ? {2}".format(target, arr, self.search(arr, target, start, end)))
        


obj = Search_in_range()
obj.input()
