# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxL = 0
        if not root:
            return 0
        def helper(root):
            if root is None:
                return 0
            left_l = helper(root.left)
            right_l = helper(root.right)
            self.maxL = max(self.maxL, left_l + right_l)
            return max(left_l, right_l) + 1
        helper(root)
        return self.maxL

        
