import sys

class Search:
    def solution(self, n, matrix, target):
        row = 0
        col = n-1
        while(col>-1 and row < n):
            if(target == matrix[row][col]):
                print("Element Found at ", end = " ")
                return ([row, col])
            elif(target < matrix[row][col]):
                col -= 1
            else:
                row += 1
        print("Element not Found")
        return [-1, -1]
        
    
    def input(self):
        print("Enter the order of the matrix")
        n = int(sys.stdin.readline().strip())
        print("Enter the target")
        target = int(sys.stdin.readline().strip())
        print("Enter 2D array")
        input = sys.stdin.readline()
        input = list(map(int, input.strip().split()))
        matrix = []
        start = 0
        
        for i in range(n):
            x = input[start:start+n]
            matrix.append(x)
            start += n
        print("n = {0} Matrix = {1}".format(n, matrix))
        print(self.solution(n, matrix, target))
        
        
obj = Search()
obj.input()
