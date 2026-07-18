# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        result = []
        while queue:
            level = len(queue)
            level_arr = []
            for i in range(level):                
                node = queue.popleft()
                if not node:
                    continue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_arr.append(node.val)
            if len(level_arr) > 0:
                result.append(level_arr)
        return result                