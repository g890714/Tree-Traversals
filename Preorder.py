# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        else:
            result = [root.val]
            left = self.preorderTraversal(root.left)
            result.extend(left)
            right = self.preorderTraversal(root.right)
            result.extend(right)
            return result
