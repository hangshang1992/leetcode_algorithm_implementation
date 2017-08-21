class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        res = [[float("inf") for _ in range(3)] for _ in range(n+1)]
        res[0][0] = 0
        res[0][1] = 0
        res[0][2] = 0
        for i in range(1, len(costs) + 1):
            for j in range(3):
                for k in range(3):
                    if j != k:
                        res[i][j] = min(res[i][j], res[i-1][k] + costs[i-1][j]) 
        return min(res[n][2], res[n][1], res[n][0])
