# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def maxLevelSum(root: Optional[TreeNode]) -> int:
    ls = []

    def dfs(n, l):
        if not n: return
        
        if l == len(ls): ls.append(0)
        
        ls[l] += n.val
        
        dfs(n.left, l + 1)
        dfs(n.right, l + 1)

    dfs(root, 0)
    
    return ls.index(max(ls)) + 1 # (26 ms)