# https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

def maximumAmount(coins: list[list[int]]) -> int:
    m, n = len(coins), len(coins[0])

    dp = [[[float('-inf')] * 3 for _ in range(n)] for _ in range(m)]
    
    dp[0][0][2] = coins[0][0]

    if coins[0][0] < 0:
        dp[0][0][1] = 0
        
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0: continue
            
            for k in range(3):
                r = float('-inf')

                if i > 0: r = max(r, dp[i - 1][j][k])
                if j > 0: r = max(r, dp[i][j - 1][k])
                if r != float('-inf'):
                    dp[i][j][k] = max(dp[i][j][k], r + coins[i][j])
                if k < 2 and coins[i][j] < 0:
                    a = float('-inf')
                    
                    if i > 0: a = max(a, dp[i - 1][j][k + 1])
                    if j > 0: a = max(a, dp[i][j - 1][k + 1])

                    dp[i][j][k] = max(dp[i][j][k], a)
                    
    return max(dp[m - 1][n - 1]) # (3979 ms)