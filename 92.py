# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or m >= n or m < 0 or n < 0:
            return head
        
        pre = h = ListNode(0)
        h.next = head
        cur = head
        i = 1
        while i < m and cur != None:
            pre = cur
            cur = cur.next
            i += 1
        
        t1 = pre
        t2 = cur
        while i <= n and cur != None:
            last = cur.next
            cur.next = pre
            pre = cur
            cur = last
            i += 1
        
        t1.next = pre
        t2.next = cur
        return h.next
