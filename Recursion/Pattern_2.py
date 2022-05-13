'''
Pattern
*
* *
* * *
* * * *
'''
class pattern2:
    def solve(self, row, column):
        if(row == 0):
            return
        if(column == row):
            self.solve(row-1, 0)
            print()
        else:
            self.solve(row, column+1)
            print("*", end = " ")
        


obj = pattern2()
obj.solve(4,0)
