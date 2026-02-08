# https://leetcode.com/problems/balanced-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root: Optional[TreeNode]) -> bool:
    def height(root):
        if root is None: return 0

        l, r = height(root.left), height(root.right)

        if l == -1 or r == -1 or abs(l - r) > 1: return -1

        return 1 + max(l, r)

    return height(root) >= 0 # (0 ms)