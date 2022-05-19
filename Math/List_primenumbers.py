import sys
import math

class Prime:
    def find(self, num):
        lst = [2]
        for i in range(3, num, 2):
            if(self.prime(i)):
                lst.append(i)
        print("All prime numbers from 2 to {0} is/are {1}".format(num, lst))

    def method_2(self, num):
        arr = [True for i in range(num+1)]
        for i in range(2,int( math.sqrt(num))+1):
            if(arr[i]):
                self.set_array(i, num, arr)
        lst = []
        for i in range(2, num):
            if(arr[i]):
                lst.append(i)
        print("All prime numbers from 2 to {0} is/are {1}".format(num, lst))

    def set_array(self, start, end, arr):
        for i in range(start+start, end+1, start):
            arr[i] = False
        #print("After setting mutiples of {0} is {1}".format(start, arr))
       
    def prime(self, num):
        for i in range(2, int(math.sqrt(num))+1):
            if(num%i == 0):
                return False
        return True

    def read_input(self):
        print("Enter Number")
        num = int(sys.stdin.readline())
        print("Input Number:", num)
        self.method_2(num)

obj = Prime()
obj.read_input()
#print(obj.prime(2))
