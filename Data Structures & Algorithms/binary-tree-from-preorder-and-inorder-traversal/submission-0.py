# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_map = {val: idx for idx, val in enumerate(inorder)}
        preorder_idx = 0
        def build(left: int, right: int):
            nonlocal preorder_idx
            if left > right:
                return None
            root_val = preorder[preorder_idx]
            preorder_idx += 1
            root = TreeNode(val=root_val)
            mid = preorder_map[root_val]
            root.left = build(left, mid-1)
            root.right = build(mid+1, right)
            return root
        return build(0, len(inorder)-1)