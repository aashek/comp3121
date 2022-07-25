import math
import sys

def maximumCoin(mat, m, n):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        dp[0][i] = mat[0][i]
        dp[i][0] = mat[i][0]

    for j in range(1,m):
        for k in range(n):       
            dp[j][k] = mat[j][k] + max(dp[j-1][k], dp[j][k-1]) 

    return dp[m-1][n-1]

def maxCoinsProb(mat, m, n, prob):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = 1

    for i in range(1,n):
        dp[0][i] = prob*dp[0][i-1]
        dp[i][0] = (1-prob)*dp[i-1][0]

    for j in range(1,m):
        for k in range(1,n):
            if k != n or j != n:       
                dp[j][k] = prob*dp[j-1][k] + (1-prob)*dp[j][k-1]


    # print(dp)
    printMat(dp)

    retSum = 0
    for j in range(m):
        for k in range(n):
            retSum += dp[j][k]*mat[j][k]
    return retSum


def printMat(m):
    for i in m:
        print(i)



m, n = [int(i) for i in input().strip().split()]
arr = []
for j in range(m):
    a = [int(i) for i in input().strip().split()]
    arr.append(a)

# print(maximumCoin(arr, m, n))
print(maxCoinsProb(arr, m, n, 0.6))