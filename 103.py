# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        level = [root]
        flag = 1
        while root and level:
            res.append([node.val for node in level][::flag])
            temp = [(node.left, node.right) for node in level]
            level = [leaf for LR in temp for leaf in LR if leaf]
            flag *= -1
        return res
