# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        res = []
        while queue:
            width = len(queue)
            for i in range(width):
                node = queue.popleft()
                if not node:
                    continue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == width - 1:
                    res.append(node.val)
        return res
