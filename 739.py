class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        next1 = [0] * 101
        waits = [0] * n
        for i in range(n-1, -1, -1):
            mark = float('inf')
            for t in range(temperatures[i] + 1, 101):
                if next1[t] != 0:
                    mark = min(mark, next1[t])
            if mark != float('inf'):
                waits[i] = mark - i
            next1[temperatures[i]] = i
        return waits
