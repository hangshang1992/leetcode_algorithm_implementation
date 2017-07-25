"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: buttom-up level order in a list of lists of integers
    """
    def levelOrderBottom(self, root):
        # write your code here
        res, level = [], [root]
        while root and level:
            res.append([node.val for node in level])
            temp = [(node.left, node.right) for node in level]
            level = [leaf for LR in temp for leaf in LR if leaf]
        return res[::-1]
