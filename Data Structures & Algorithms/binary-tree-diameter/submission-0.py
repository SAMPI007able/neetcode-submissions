# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l_max = self.max_height(root.left)
        r_max = self.max_height(root.right)
        diam = l_max + r_max
        child_diam = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(diam, child_diam)

    def max_height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + max(self.max_height(node.left), self.max_height(node.right))


        
