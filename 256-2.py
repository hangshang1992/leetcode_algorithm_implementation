class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0])
        res = [[float('inf') for _ in range(k)] for _ in range(n + 1)]
        for i in range(k):
            res[0][i] = 0
        for i in range(1, n+1):
            for j in range(k):
                for x in range(k):
                    if j != x:
                        res[i][j] = min(res[i][j], res[i-1][x] + costs[i-1][j])
        return min(res[n])
