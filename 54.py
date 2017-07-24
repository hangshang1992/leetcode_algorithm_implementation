class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]: return []
        res = []
        i, di, j, dj = 0,0,0,1
        m,n = len(matrix), len(matrix[0])
        for _ in range(m*n):
            res.append(matrix[i][j])
            matrix[i][j] = ""
            if matrix[(i + di)%m][(j+dj)%n] == "":
                di, dj = dj, -di
            i += di
            j += dj
        return res
