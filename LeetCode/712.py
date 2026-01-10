# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

def minimumDeleteSum(s1: str, s2: str) -> int:
    n_s1, n_s2 = len(s1), len(s2)
    dp = {} # (i, j) being the answer for inputs s1[i:] and s2[j:]

    def dfs(i, j):
        if (i, j) in dp: return dp[(i, j)] # Memoization check
        
        t = 999999999999999999999999

        if i >= n_s1 and j >= n_s2: return 0
        if i >= n_s1: return sum([ord(s2[k]) for k in range(j, n_s2)]) 
        if j >= n_s2: return sum([ord(s1[k]) for k in range(i, n_s1)])

        if s1[i] == s2[j]: t = min(t, dfs(i + 1, j + 1))
        
        t = min(t, ord(s1[i]) + dfs(i + 1, j), ord(s2[j]) + dfs(i, j + 1))
        dp[(i, j)] = t

        return dp[(i, j)]

    return dfs(0, 0) # (1041 ms)