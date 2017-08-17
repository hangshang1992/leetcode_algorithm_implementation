# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        while start.next:
            end = start
            for _ in range(k-1):
                end = end.next
                if end.next == None:
                    return dummy.next
            res = self.reverse(start.next, end.next)
            start.next = res[0]
            start = res[1]
        return dummy.next
    def reverse(self, start, end):
        dummy1 = ListNode(0)
        dummy1.next = start
        while dummy1.next != end:
            temp = start.next
            start.next = temp.next
            temp.next = dummy1.next
            dummy1.next = temp
        return [end, start]
