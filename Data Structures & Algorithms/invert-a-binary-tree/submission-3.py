# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    is_iterative = False
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not self.is_iterative: 
            if not root:
                return root        
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root
        else:
            queue = deque([root])
            while queue:
                node = queue.popleft()
                if not node:
                    return None
                node.left, node.right = node.right, node.left
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return root