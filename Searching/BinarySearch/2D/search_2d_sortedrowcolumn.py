import sys

class Search:
    def solution(self, matrix, target):
        row = 0
        col = len(matrix[0])-1
        while(col>-1 and row < len(matrix)):
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
        order = list(map(int, ((sys.stdin.readline().strip().split()))))
        n, m = order[:2]
        print("Enter the target")
        target = int(sys.stdin.readline().strip())
        print("Enter 2D array")
        input = sys.stdin.readline()
        input = list(map(int, input.strip().split()))
        matrix = []
        start = 0
        
        for i in range(n):
            x = input[start:start+m]
            matrix.append(x)
            start += m
        print("n = {0} m = {1} Matrix = {2}".format(n, m, matrix))
        print(self.solution(matrix, target))
        
        
        
obj = Search()
obj.input()
