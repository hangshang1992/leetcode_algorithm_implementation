# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        stack, set1 = [root], set()
        while stack:
            node = stack.pop()
            if k - node.val in set1:
                return True
            set1.add(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return False
