# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def doValidate(node, low, high):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return doValidate(node.left, low, node.val) and doValidate(node.right, node.val, high)
        return doValidate(root, float('-inf'), float('inf'))