# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq 
        pairs = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(pairs)
        dummy = ListNode(0)
        cur = dummy
        while len(pairs) != 0:
            value, i, node = heapq.heappop(pairs)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(pairs, (node.next.val, i, node.next))
        return dummy.next
