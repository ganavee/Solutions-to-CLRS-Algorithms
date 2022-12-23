#To print first n Fibonacci Numbers

def fiboRec(first, sec, count, n):
    if(count == n):
        return
    print(first + sec)
    fiboRec(sec, first+sec, count + 1, n)

def fibonacci(n):
    if(n == 0):
        return
    print(0)
    if(n == 1):
        return
    print(1)
    fiboRec(0, 1, 2, n)

print("First N fibonacci series is: ")
fibonacci(3)

#To print nth fibonaaci number
def nthFiboRec(first, sec, count, n):
    if(count == n):
        return sec
    return nthFiboRec(sec, first+sec, count + 1, n)

def nthFib(n):
    if(n == 0):
        return
    if(n == 1):
        return 0
    if(n == 2):
        return 1
    return nthFiboRec(0, 1, 2, n)

print("Nth Fibonacci number: ",nthFib(4))

#To print fibobacci uptil n

def uptilFiboRec(first, sec, n):
    if((first + sec) > n):
        return
    print(first + sec)
    uptilFiboRec(sec, first + sec, n)

def uptilFib(n):
    if(n == 0):
        return
    print(0)
    if(n == 1):
        return
    print(1)
    uptilFiboRec(0, 1, n)

print("Fibo uptil given number: ")
uptilFib(10)
