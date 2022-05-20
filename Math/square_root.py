import sys
import math

class SquareRoot:
    def find(self, num):
        lst = self.primes(num)
        print("Primes ", lst)
        n = num
        sqrt = 1
        for i in lst:
            while(num%i == 0):
                sqrt *= i
                num = num/(i*i)
            if(num == 1):
                break
        print("Square root of a perfect square {0} is {1}".format(n, sqrt))

    def primes(self, num):
        arr = [[True, i] for i in range((num+1)//2)]
        lst = []
        for i in range(2, int(math.sqrt(num)) + 1):
            if(arr[i]):
                for j in range(i*2, (num+1)//2, i):
                    arr[j][0] = False
        for i in range(2, (num+1)//2):
            if(arr[i][0]):
                lst.append(i)
        return lst

    def find2(self, start, end, n):
        mid = (start+end)//2
        if(mid*mid > n):
            end = mid -1
        elif(mid*mid < n):
            start = mid+1
        else:
            return mid
        return self.find2(start, end, n)

    def perfect_sqrt(self, num):
        sqrt = self.find2(1, num, num)
        print("Square root of {0} is {1}".format(num, sqrt))
    
    def read_input(self):
        print("Enter Number")
        num = int(sys.stdin.readline())
        print("Input Number:", num)
        #self.find(num)
        self.perfect_sqrt(num)

obj = SquareRoot()
obj.read_input()
