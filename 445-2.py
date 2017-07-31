# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return l1
        val1 = 0
        while(l1 != None):
            val1 = l1.val + val1*10
            l1 = l1.next

        val2 = 0
        while(l2 != None):
            val2 = l2.val + val2*10
            l2 = l2.next

        sum = val1+val2
        head = ListNode(0)
        while(sum!=0):
          v = sum%10
          head.val = v
          node = ListNode(sum/10)
          node.next =head
          head = node
          sum = sum/10
        return head.next if (val1+val2) !=0 else head
