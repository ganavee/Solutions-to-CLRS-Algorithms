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
        elif(mid*mid == n):
            return mid
        return self.find2(start, end, n)

    def perfect_sqrt(self, num):
        sqrt = self.find2(1, num, num)
        print("Square root of {0} is {1}".format(num, sqrt))

    def decimal_part(self, incr, rounded, k, n, places, count):
        #print(" before incr {0} k {1}".format(incr, k))
        k = round(k, rounded)
        incr = round(incr, rounded)
        if(k*k < n):
            #print("Hello k {0} incr {1}".format(k, incr))
            return self.decimal_part(incr, rounded, (k+incr), n, places, count)
        else:
            if(count == places):
                return k-incr
            count += 1
            return self.decimal_part(incr*0.1, rounded+1, (k-incr)+(incr*0.1), n, places, count)

    def find3(self, start, end, n, places):
        if(start >= end):
            if(start*start == n):
                return start
            elif(start*start < n):
                return self.decimal_part(0.1, 1, start+0.1, n, places, 1)
            else:
                return self.decimal_part(0.1, 1, start-1+0.1, n, places, 1)
        mid = (start+end)//2
        #print("mid ", mid)
        if(mid*mid > n):
            end = mid - 1
        elif(mid*mid < n):
            start = mid + 1
        elif(mid*mid == n):
            return mid
        return self.find3(start, end, n, places)

    def imperfect_sqrt(self, num, places ):
        return self.find3(1, num, num, places)
        pass
    
    def read_input(self):
        print("Enter Number and decimal places")
        arr = (sys.stdin.readline())
        arr = list(map(int, arr.strip().split()))
        num = arr[0]
        places = arr[1]
        print("Input Number: {0} decimal places {1}".format(num, places))
        #self.find(num)
        integer = self.imperfect_sqrt(num, places)
        print("Square root of {0} is {1} ".format(num, integer))

obj = SquareRoot()
obj.read_input()
