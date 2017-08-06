# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        queue, nextLevel = [root], []
        while queue:
            curr = queue.pop(0)
            if curr.left:
                nextLevel.append(curr.left)
            if curr.right:
                nextLevel.append(curr.right)
            if queue:
                curr.next = queue[0]
            if not queue and nextLevel:
                queue, nextLevel = nextLevel, queue
