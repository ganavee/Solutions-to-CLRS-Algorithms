class Solution:
    #Memoization
    def sol(self, n, count, dp, i):
        #print(f"Firsti = {i}n = {n} count = {count} dp = {dp}")
        if(n == 0):
            return count+1
        if(n < 0):
            return count
        if(dp[n] != -1):
            return count + dp[n]
        #print(f"second i = {i}n = {n} count = {count} dp = {dp}")
        count = self.sol(n-1, count, dp, i+1)
        #print(f"Third i = {i}n = {n} count = {count} dp = {dp}")
        count = self.sol(n-2, count, dp, i+1)
        dp[n] = count
        #print(f"Forth i = {i} n = {n} count = {count} dp = {dp}")
        return count
    
    #Tabulation
    def sol1(self, n, dp):
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    
    
    def climbStairs(self, n):
        dp = [-1 for i in range(n+1)]
        
        print(f"Solution1: {self.sol(n, 0, dp, 1)}")
        print(f"Solution2: {self.sol1(n, dp)}")

obj =  Solution()
obj.climbStairs(40)
