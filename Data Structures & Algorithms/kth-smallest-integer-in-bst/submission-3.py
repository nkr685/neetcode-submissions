# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0

        def traverse(root: Optional[TreeNode]):
            nonlocal k, res
            if not root:
                return

            traverse(root.left)
            k -= 1
            if k == 0:
                res = root.val
            elif k > 0:
                traverse(root.right)
        traverse(root)
        return res
