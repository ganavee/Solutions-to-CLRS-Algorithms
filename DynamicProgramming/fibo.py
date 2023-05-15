#Memoisation
#TC = O(N)
#SC = O(N)(recursion stack) + O(N)(dp)
def fibo(n, dp):
    if(n < 2):
        return n
    if(dp[n] != -1):
        return dp[n]
    dp[n] = fibo(n-1, dp) + fibo(n-2, dp)
    return dp[n]

#Tabulation
#TC = O(N)
#SC =O(N)(dp)
def fibo1(n, dp, i):
    if(n < 2 ):
        return dp[n]
    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]

#TC = O(N)
#SC =O(1)
def fibo2(n):
    if(n < 2):
        return n
    first = 0
    second  = 1
    for i in range(2, n+1):
        first, second = second, first+second
    return second

n = 7
dp = [-1 for i in range(n+1)]
dp[0] = 0
if(n != 0):
    dp[1] = 1
print("Fibo: ",fibo(n,dp))
print("Fibo1: ",fibo1(n,dp, 2))
print("Fibo2: ",fibo2(n))
