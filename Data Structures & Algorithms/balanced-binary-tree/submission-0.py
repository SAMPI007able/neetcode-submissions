# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:        
        is_bal = True
        def compute_height(node):
            if not node:
                return 0
            l_height = compute_height(node.left)
            if l_height == -1:
                return -1
            r_height = compute_height(node.right)
            if r_height == -1 :
                return -1
           
            if abs(l_height - r_height) > 1:
                return -1
            return 1 + max(l_height, r_height)
        
        return compute_height(root) != -1