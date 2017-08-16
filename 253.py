# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        from heapq import *
        intervals.sort(key=lambda i:i.start)
        pq=[]
        res=0
        for i in intervals:
            """
            pop meetings already end
            """
            while pq and pq[0]<=i.start:
                heappop(pq)
            heappush(pq,i.end)
            print pq
            res=max(res,len(pq))
        return res
