# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def check_good_node_with_boundary(node, high):             
            if not node:
                return 0
            good = 1 if high <= node.val else 0
            high = max(node.val, high)
            # if high <= node.val:                
            #     high = node.val
            #     res.append(node.val)
            return good + check_good_node_with_boundary(node.left, high) + check_good_node_with_boundary(node.right, high)
                
        return check_good_node_with_boundary(root, root.val)