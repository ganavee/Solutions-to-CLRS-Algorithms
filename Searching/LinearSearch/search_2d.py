import sys
class Search_in_range:
    def search(self, a, target):
        print("hey")
        for i in range(len(a)):
            for j in a[i]:
                if(j == target):
                    return True
        return False
    
    def input(self):
        print("Enter 2D Array")
        print("Enter 0 to end and 1 to continue")
        input = int(sys.stdin.readline())
        a = []
        while(input):
            print("Enter the row of elements")
            arr = list(map(int, sys.stdin.readline().strip().split()))
            a.append(arr)
            print("Enter 0 to end and 1 to continue")
            input = int(sys.stdin.readline())
        print("Enter number to be searched")
        target = int(sys.stdin.readline())
        print("Input arr = {0} and target is {1} ".format(a, target))
        print("Is {0} present in {1} ? {2}".format(target, a, self.search(a, target)))
        


obj = Search_in_range()
obj.input()
