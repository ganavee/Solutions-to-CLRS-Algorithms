import sys
class LCM:
    def gcd(self, num1, num2):
        if(num2 == 0):
            return num1
        return self.gcd(num2, num1%num2)
    
    def lcm(self, num1, num2):
        if(num1>num2):
            hcf = self.gcd(num1, num2)
        else:
            hcf = self.gcd(num2, num1)
        return((num1*num2)/hcf)
    
    def input(self):
        print("Enter 2 input numbers")
        arr = sys.stdin.readline()
        arr = list(map(int, arr.strip().split()))
        num1 = arr[0]
        num2 = arr[1]
        print("Input numbers are {0} and {1}".format(num1, num2))
        #print(self.gcd(num1, num2))
        print("LCM of {0} and {1} is {2}".format(num1, num2, int(self.lcm(num1, num2))))
        

obj = LCM()
obj.input()
