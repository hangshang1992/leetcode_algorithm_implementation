class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0 or len(costs[0]) == 0:
            return 0
        n = len(costs)
        k = len(costs[0])
        res = [[float('inf') for _ in range(k)] for _ in range(n + 1)]
        for i in range(k):
            res[0][i] = 0
        for i in range(1, n+1):
            min1 = min2 = float('inf')
            j1 = j2 = -1
            for j in range(k):
                if res[i-1][j] < min1:
                    min2 = min1
                    j2 = j1
                    min1 = res[i-1][j]
                    j1 = j
                elif res[i-1][j] < min2:
                    min2 = res[i-1][j]
                    j2 = j
            for j in range(k):
                if j != j1:
                    res[i][j] = costs[i-1][j] + res[i-1][j1]
                else:
                    res[i][j] = costs[i-1][j] + res[i-1][j2]
        return min(res[n])
