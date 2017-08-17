class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def timeCompute(p):
            h, m = map(int, p.split(":"))
            return h*60 + m
        timePoints = sorted(map(timeCompute, timePoints))
        timePoints.append(24*60+timePoints[0])
        return min(b-a for a,b in zip(timePoints, timePoints[1:]))
