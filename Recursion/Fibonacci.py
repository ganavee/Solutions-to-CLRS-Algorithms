class Fibonacci:
    def nth_fibonacci(self, first, second, count, n):
        if(n == 1):
            return 0
        elif(n == 2):
            return 1
        elif(count == n):
            return(first+second)
        return self.nth_fibonacci(second, first+second, count+1, n)

    def fibo(self, num):
        if(num == 1):
            return 0
        if(num == 2):
            return 1
        return self.fibo(num-1)+self.fibo(num-2)


obj = Fibonacci()
n = 5
print("{0}th Fibonnaci number is {1}".format(n, obj.nth_fibonacci(0, 1, 3, n)))
print("{0}th Fibonnaci number is {1}".format(n, obj.fibo(n)))
