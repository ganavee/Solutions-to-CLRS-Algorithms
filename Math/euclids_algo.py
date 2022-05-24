import sys
class Eudclid:
    def gcd(self, num1, num2):
        if(num2 == 0):
            return num1
        mod = num1%num2
        return self.gcd(num2, mod)
        
    
    def input(self):
        print("Enter 2 input numbers")
        arr = sys.stdin.readline()
        arr = list(map(int, arr.strip().split()))
        num1 = arr[0]
        num2 = arr[1]
        print("Input numbers are {0} and {1}".format(num1, num2))
        if(num1>num2):
            value = self.find(num1, num2)
        else:
            value = self.gcd(num2, num1)
        print("GCD of {0} and {1} is {2}".format(num1, num2, value))

obj = Eudclid()
obj.input()
