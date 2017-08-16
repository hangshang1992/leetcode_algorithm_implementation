# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        res = -1
        for i in sorted(intervals, key = lambda item : item.start):
            if res == -1:
                res = i.end
                continue
            if res > i.start:
                return False
            res = i.end
        return True
