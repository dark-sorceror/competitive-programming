# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/

def numberOfStableArrays(zero: int, one: int, limit: int) -> int:
    dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
    dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

    for i in range(1, min(zero, limit) + 1):
        dp0[i][0] = 1

    for j in range(1, min(one, limit) + 1):
        dp1[0][j] = 1

    for i in range(1, zero + 1):
        for j in range(1, one + 1):
            dp0[i][j] = (dp0[i - 1][j] + dp1[i - 1][j]) % (10**9 + 7)
            
            if i > limit:
                dp0[i][j] = (dp0[i][j] - dp1[i - limit - 1][j] + (10**9 + 7)) % (10**9 + 7)
            dp1[i][j] = (dp1[i][j-1] + dp0[i][j - 1]) % (10**9 + 7)
            if j > limit:
                dp1[i][j] = (dp1[i][j] - dp0[i][j - limit - 1] + (10**9 + 7)) % (10**9 + 7)

    return (dp0[zero][one] + dp1[zero][one]) % (10**9 + 7) # (2494 ms)