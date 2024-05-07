class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        col = [False] * m 
        row = [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    col[i] = True
                    row[j] = True 
        for i in range(m):
            for j in range(n):
                if col[i] or row[j]:
                    matrix[i][j] = 0
                    
