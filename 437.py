# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.count = 0
        def helper(root, arr):
            if not root:
                return 
            
            arr = [val_info + root.val for val_info in arr] + [root.val]
            for num in arr:
                if num == sum:
                    self.count += 1
            
            helper(root.left, arr)
            helper(root.right, arr)
        helper(root, [])
        return self.count
            
