# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = 0
        
        def dfs(node):
            if not node:
                return 0
            nonlocal diam
            l_height = dfs(node.left)
            r_height = dfs(node.right)
            diam = max(diam, l_height + r_height)
            return 1 + max(l_height, r_height)

        dfs(root)
        return diam


        
