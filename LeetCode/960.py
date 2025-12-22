# https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

def minDeletionSize(strs: list[str]) -> int:
    n, m = len(strs), len(strs[0])
        
    # dp[j] stores the length of the longest valid subsequence 
    dp = [1] * m
    
    for j in range(1, m):
        for i in range(j):
            if all(strs[k][i] <= strs[k][j] for k in range(n)):
                dp[j] = max(dp[j], dp[i] + 1)
                
    return m - max(dp) # (154 ms)