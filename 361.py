class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        up = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 'W':
                    if grid[i][j] == 'E':
                        up[i][j] = 1
                    if i > 0:
                        up[i][j] += up[i-1][j]
        down = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n):
                if grid[i][j] != 'W':
                    if grid[i][j] == 'E':
                        down[i][j] = 1
                    if i + 1 < m:
                        down[i][j] += down[i+1][j]
        left = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 'W':
                    if grid[i][j] == "E":
                        left[i][j] = 1
                    if j > 0:
                        left[i][j] += left[i][j-1]
        right = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n-1, -1, -1):
                if grid[i][j] != 'W':
                    if grid[i][j] == 'E':
                        right[i][j] = 1
                    if j + 1 < n:
                        right[i][j] += right[i][j+1]
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    result = max(result, up[i][j] + down[i][j] + left[i][j] + right[i][j])
        return result
