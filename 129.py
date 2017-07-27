# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        res = []
        self.dfs(root, [], res)
        res = [int(''.join(map(str, item))) for item in res]
        return sum(res)
    def dfs(self, root, path, res):
        if not root.left and not root.right:
            path.append(root.val)
            res.append(path)
            return
        if root.left:
            self.dfs(root.left, path + [root.val], res)
        if root.right:
            self.dfs(root.right, path + [root.val], res)
