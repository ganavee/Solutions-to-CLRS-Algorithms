from os import *
from sys import *
from collections import *
from math import *

from typing import *

#Memoization
def frog(arr, n, dp):
    if(n == 0):
        return 0
    if(dp[n] != -1):
        return dp[n]

    left = abs(arr[n] - arr[n-1]) + frog(arr, n-1, dp)
    right = maxsize
    if(n-2 >= 0):
        right = abs(arr[n] - arr[n-2]) + frog(arr, n-2, dp)
    dp[n] = min(left, right)
    #print(f"n {n} left {left} right {right} dp {dp}")
    return dp[n]


def frogJump(n: int, heights: List[int]) -> int:
    dp = [-1 for i in range(n)]
    return frog(heights, n-1, dp)
    
#Recursive solution
def rec(currStep, n, heights, minEnergy, currEnergy):
    if(currStep == n-1):
        if(minEnergy > currEnergy):
            minEnergy = currEnergy
        return minEnergy
    if(currStep > n):
        return minEnergy
    minEnergy = rec(currStep+1, n, heights, minEnergy,
                 currEnergy+abs(heights[currStep] - heights[currStep+1]))
    if(currStep+2 < n):
        minEnergy = rec(currStep+2, n, heights, minEnergy, 
                 currEnergy+abs(heights[currStep] - heights[currStep+2]))
    return minEnergy


def frogJump1(n, heights):
    #dp = [-1 for i in range(n+1)]
    print(f"Solution1: {rec(0, n, heights, maxsize, 0)}")

height = [7, 4, 4, 2, 6, 6, 3, 4] 
print(f"Solution2: {frogJump(len(height), height)}")
