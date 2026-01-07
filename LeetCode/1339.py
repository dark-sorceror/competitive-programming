# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxProduct(root: Optional[TreeNode]) -> int:
    s = []

    def dfs(n):
        if not n: return 0

        cs = n.val + dfs(n.left) + dfs(n.right)
        s.append(cs)

        return cs

    ts = dfs(root)

    m = 0

    for i in s:
        p = i * (ts - i)

        if p > m: m = p

    return m % (10**9 + 7) # (31 ms)