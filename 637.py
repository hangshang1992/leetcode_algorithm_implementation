# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        level = [root]
        while root and level:
            res.append([node.val for node in level])
            temp = [(node.left, node.right) for node in level]
            level = [leaf for LR in temp for leaf in LR if leaf]
        res = [sum(item)*1.0/len(item) for item in res]
        return res
