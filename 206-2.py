# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l1 = None
        while head:
            curr = head
            head = head.next
            curr.next = l1
            l1 = curr
        return l1
