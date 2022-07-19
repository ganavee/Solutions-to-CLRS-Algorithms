import sys

class Recursion:
    def solve(self, n, a):
        if(n == 0):
            return a
        return (self.solve(n-1, n+a))


obj = Recursion()
print("Enter a number")
input = int(sys.stdin.readline())
print("Sum of number from {0} to 1 is {1}".format(input, obj.solve(input, 0)))
