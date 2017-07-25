# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, num):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not num:
            return None

        median  = len(num)/2
        new_node = TreeNode(num[median])

        new_node.left = self.sortedArrayToBST(num[:median])
        new_node.right = self.sortedArrayToBST(num[median+1:])
        
        return new_node
