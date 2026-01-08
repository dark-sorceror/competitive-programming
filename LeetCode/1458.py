# https://leetcode.com/problems/max-dot-product-of-two-subsequences/
 
def maxDotProduct(nums1: list[int], nums2: list[int]) -> int:
    m, n = len(nums1), len(nums2)
    mdp = [[float('-inf')] * (n + 1) for i in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            p = nums1[i - 1] * nums2[j - 1]
            mdp[i][j] = max(p, mdp[i - 1][j - 1] + p, mdp[i - 1][j], mdp[i][j - 1])
            
    return mdp[m][n] # (119 ms)