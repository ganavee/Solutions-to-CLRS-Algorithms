#Recursion 0->n
def rec(subSum, sub, maxSum, arr, lastPicked, cIndex):
        #print(f"subSum={subSum} sub={sub} maxSum={maxSum} lastPicked={lastPicked} cIndex={cIndex}")
    if(len(arr) <= cIndex):
        if(subSum > maxSum):
            maxSum = subSum
        return maxSum
    #Picking
    if(lastPicked == False):
        left = rec(subSum+arr[cIndex], sub+(arr[cIndex],), maxSum, arr, 
                True, cIndex+1)
    else:
        left = rec(subSum, sub, maxSum, arr, False, cIndex+1)
    #Not Picking
    right = rec(subSum, sub, maxSum, arr, False, cIndex+1)
    maxSum = max(left, right)
    return maxSum

#Recursion n->0
def rec2(subSum, sub, maxSum, arr, cIndex):
    #print(f"subSum={subSum} sub={sub} maxSum={maxSum} cIndex={cIndex}")
    if(cIndex < 0):
        return subSum

    #Picking
    left = rec2(subSum+arr[cIndex], sub+(arr[cIndex],), maxSum, arr,
             cIndex-2)

    #Not Picking
    right = rec2(subSum, sub, maxSum, arr, cIndex-1)
    #print(f"left {left} right {right}")
    
    return max(left, right)

#Memo
def memo(subSum, sub, maxSum, arr, cIndex, dp, i):
     #print(f"F{i} subSum={subSum} sub={sub} maxSum={maxSum} cIndex={cIndex} dp={dp}")
    if(cIndex < 0):
        return subSum

    if(dp[cIndex] != -1):
        return dp[cIndex]
    #Picking
    #print(f"S{i} subSum={subSum} sub={sub} maxSum={maxSum} cIndex={cIndex} dp={dp}")
    left = subSum+arr[cIndex] + memo(subSum, sub+(arr[cIndex],),
             maxSum, arr, cIndex-2, dp, i+1)

    #Not Picking
    #print(f"T{i} subSum={subSum} sub={sub} maxSum={maxSum} cIndex={cIndex} dp={dp}")
    right = memo(subSum, sub, maxSum, arr, cIndex-1, dp, i+1)
    #print(f"left {left} right {right}")
    
    dp[cIndex] = max(left, right)
    #print(f"Fo{i} subSum={subSum} sub={sub} maxSum={maxSum} cIndex={cIndex} dp={dp} left={left} right={right}")
    return dp[cIndex]


#Tabulation
def tabulation(arr):
    n = len(arr)
    dp = [-1 for i in range(n)]
    dp[0] = arr[0]
    if(n > 1):
        dp[1] = arr[1]
    #print(f"tab dp={dp}")
    for i in range(2, n):
        maximum = dp[0]
        for j in range(1, i-1):
            maximum = max(maximum, dp[j])
        dp[i] = maximum + arr[i]
        #print(f"dp={dp} max={maximum} i={i}")
    return max(dp[n-1], dp[n-2])

#Another tabulation
def tab2(arr):
    n = len(arr)
    dp = [-1 for i in range(n)]
    dp[0] = arr[0]
    for i in range(1, n):
        pick = arr[i]
        if(i-2 >= 0):
            pick += dp[i-2]
        noPick = 0 + dp[i-1]
        dp[i] = max(pick, noPick)
    return dp[n-1]

#Space Optimisation
def space(arr):
    n = len(arr)
    second = arr[0]
    for i in range(1, n):
        pick = arr[i]
        if(i-2 >= 0):
            pick += first
        noPick = 0 + second
        first = second
        second = max(pick, noPick)
    return second

#Space Optimization
def space2(arr):
    n = len(arr)
    maximum1 = arr[0]
    if(n > 1):
        maximum2 = arr[1]
    else:
        return maximum1
    #print(f"tab dp={dp}")
    for i in range(2, n):
        curr = max(maximum1 + arr[i])
        maximum1 = maximum2
        maximum2 = curr
        print(f"max1={maximum1} max2={maximum2} i={i}")
    return max(maximum1, maximum2)

arr = (2,1,4,9)
print(f"Solution recursion: {rec(0, (), 0, arr, False, 0)}")

print(f"Solution recursion2: {rec2(0, (), 0, arr, len(arr)-1)}")
dp = [-1 for i in range(len(arr))]
print(f"Solution Memo: {memo(0, (), 0, arr, len(arr)-1, dp, 1)}")
#print(f"Memo dp={dp}")
print(f"Solution tab: {tabulation(arr)}")
print(f"Solution tab2: {tab2(arr)}")
#rint(f"Solution Space: {space(arr)}")
