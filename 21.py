# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: return l2
        if not l2: return l1
        l3 = h3 = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                l3.next = ListNode(l2.val)
                l3, l2 = l3.next, l2.next
            else:
                l3.next = ListNode(l1.val)
                l3, l1 = l3.next, l1.next
        l3.next = l1 or l2
        return h3.next
