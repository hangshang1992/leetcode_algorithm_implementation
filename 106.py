# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder: return None
        root = TreeNode(postorder[-1])
        index_a = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:index_a], postorder[:index_a])
        root.right = self.buildTree(inorder[index_a+1:], postorder[index_a:-1])
        return root
