'''
Pattern 1
* * * *
* * *
* *
*
'''
class Pattern1:
    def solve_recursion(self, n):
        if(n == 0):
            return
        for i in range(n, 0, -1):
            print("*", end = " ")
        print()
        self.solve_recursion(n-1)

    def solve_recursion_complete(self, row, column, col_start):
        if(row == 0):
            return
        if(col_start == column):
            print()
            self.solve_recursion_complete(row-1, column-1, 0)
        else:
            print("*", end = " ")
            self.solve_recursion_complete(row, column, col_start+1)

    def solve_recursion_alternate(self, row, col):
        if(row == 0):
            return
        if(col == row):
            print()
            self.solve_recursion_alternate(row-1, 0)
        else:
            print("*", end = " ")
            self.solve_recursion_alternate(row, col+1)

    def solve_iteration(self):
        for i in range(4, 0, -1):
            for i in range(0, i):
                print("*", end = " ")
            print()
    
obj = Pattern1()
#obj.solve_iteration(4)
obj.solve_recursion(4)
obj.solve_recursion_complete(4,4, 0)
obj.solve_recursion_alternate(4, 0)
