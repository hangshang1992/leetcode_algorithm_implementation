# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def collect(root,depth):
            if not root: 
                return
            if depth == len(res):
                res.append(root.val)
            collect(root.right, depth+1)
            collect(root.left, depth + 1)
        res = []
        collect(root,0)
        return res
