from os import *
from sys import *
from collections import *
from math import *

from typing import *


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
    
