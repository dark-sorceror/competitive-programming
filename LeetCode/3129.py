# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/

def numberOfStableArrays(zero: int, one: int, limit: int) -> int:
    dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
    
    for i in range(1, min(zero, limit) + 1):
        dp[i][0][0] = 1

    for j in range(1, min(one, limit) + 1):
        dp[0][j][1] = 1
        
    for i in range(1, zero + 1):
        for j in range(1, one + 1):
            dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % (10 ** 9 + 7)

            if i > limit:
                dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + (10**9 + 7)) % (10 ** 9 + 7)
                
            dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % (10 ** 9 + 7)

            if j > limit:
                dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + (10**9 + 7)) % (10 ** 9 + 7)
                
    return (dp[zero][one][0] + dp[zero][one][1]) % (10 ** 9 + 7) # (195 ms)