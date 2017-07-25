# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(root):
            if not root: return 0
            right = helper(root.right)
            left = helper(root.left)
            if right == -1 or left == -1 or abs(right - left) > 1:
                return -1
            return 1 + max(right,left)
        return helper(root) != -1
