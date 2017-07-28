# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder: return None
        root = TreeNode(preorder[0])
        index_a = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index_a+1], inorder[:index_a])
        root.right = self.buildTree(preorder[index_a+1:], inorder[index_a+1:])
        return root
