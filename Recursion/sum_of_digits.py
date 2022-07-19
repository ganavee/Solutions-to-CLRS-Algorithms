import sys

class Recursion:
    def tail_recursion(self, n, a):
        if(n == 0):
            return a
        return (self.tail_recursion(n//10, (n%10)+a))

    def non_tail_recursion(self, n):
        if(n == 0):
            return 0
        return (n%10) + self.non_tail_recursion(n//10)


obj = Recursion()
print("Enter a number")
input = int(sys.stdin.readline())
print("Sum of digits {0} is {1} using Non Tail Recursion".format(input, obj.non_tail_recursion(input)))
print("Sum of digits {0} is {1} using Tail Recursion".format(input, obj.tail_recursion(input, 0)))
