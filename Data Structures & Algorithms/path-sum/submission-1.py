# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def traverse(root: Optional[TreeNode], currentSum: int) -> bool:
            nonlocal targetSum
            newSum = currentSum + root.val
            
            if not root.left and not root.right:
                if newSum == targetSum:
                    return True
                else:
                    return False
            lb = rb = False
            if root.left:
                lb = traverse(root.left, newSum)
            if root.right:
                rb = traverse(root.right, newSum)
            return lb or rb

        return traverse(root, 0)