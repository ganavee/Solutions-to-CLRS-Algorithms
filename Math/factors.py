import math
import sys

class Factors:
    #T = sqrt(n)
    def factor_opti(self, num):
        lst = []
        for i in range(1, int(math.sqrt(num))+1):
            if(num%i == 0):
                lst.append(i)
                if(num//i != i):
                    lst.append(num//i)
        return lst

    def factor_opti_sort(self, num):
        lst = []
        lst1 = []
        for i in range(1, int(math.sqrt(num))+1):
            if(num%i == 0):
                lst.append(i)
                if(num//i != i):
                    lst1.insert(0,num//i)
        return lst+lst1
    
    def factor(self, num):
        lst = []
        for i in range(1, num+1):
            if(num%i == 0):
                lst.append(i)
        return lst
    
    def input(self):
        print("Enter a number")
        num = int(sys.stdin.readline())
        print("Number is ", num)
        print("1: Factors of {0} is {1} ".format(num, self.factor(num)))
        print("2: Factors of {0} is {1} ".format(num, self.factor_opti_sort(num)))

obj = Factors()
obj.input()
