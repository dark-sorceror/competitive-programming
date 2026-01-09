from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def subtreeWithAllDeepest(root: Optional[TreeNode]) -> Optional[TreeNode]:
    def dfs(n):
        if not n: return (0, None)

        ld, lr = dfs(n.left)
        rd, rr = dfs(n.right)

        if ld > rd: return (ld + 1, lr)
        elif rd > ld: return (rd + 1, rr)
        else: return (ld + 1, n)

    return dfs(root)[1] # (0 ms)