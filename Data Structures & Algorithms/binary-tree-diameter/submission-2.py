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
        height = {None: 0}
        stack = []
        curr = root
        diam = 0
        last_visited = None
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack[-1]
            if node.right and last_visited != node.right:
                curr = node.right
                continue
            stack.pop()
            l_height = height[node.left]
            r_height = height[node.right]

            diam = max(l_height + r_height, diam)
            height[node] = 1 + max(l_height, r_height)
            last_visited = node
        return diam


        
