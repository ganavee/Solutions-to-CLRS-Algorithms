import sys

class Recursion:
    def tail_recursion(self, n, a):
        if(n == 0):
            return a
        if(n%10 == 0):
            return (self.tail_recursion(n//10, a+1))
        else:
            return(self.tail_recursion(n//10,a))

    def non_tail_recursion(self, n):
        if(n == 0):
            return 0
        if(n%10 == 0):
            return 1 + self.non_tail_recursion(n//10)
        else:
            return 0 + self.non_tail_recursion(n//10)


obj = Recursion()
print("Enter a number")
input = int(sys.stdin.readline())
print("Number of 0's in {0} is {1} using Non Tail Recursion".format(input, obj.non_tail_recursion(input)))
print("Number of 0's in {0} is {1} using Tail Recursion".format(input, obj.tail_recursion(input, 0)))
