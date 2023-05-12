#Using Single Recursive Call
#TC = O(n)
def fib(n, first, arr):
    if(n == 0):
        return arr
    arr.append(arr[first] + arr[first+1])
    return fib(n-1, first+1, arr)

#Using Multiple Recursive Call
#TC = nearly O(2^n)
def fib2(n):
    if(n == 0 or n == 1):
        return n
    return fib2(n-1) + fib2(n-2)

n = int(input("Enter n: "))
arr = [0, 1]
if(n == 0):
    print(f"Fibonacci of first {n} numbers is []")
elif(n == 1):
    print(f"Fibonacci of first {n} numbers is 0")
elif(n == 0):
    print(f"Fibonacci of first {n} numbers is [0, 1]")
else:
    print(f"First: Fibonacci of first {n} numbers is {fib(n-2, 0, arr)}")
print(f"Second: {n}th Fibonnaci number is {fib2(n)}", end = " ")  
