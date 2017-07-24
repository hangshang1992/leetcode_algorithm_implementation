class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i<j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for item in matrix:
            for i in range(len(item)/2):
                item[i], item[~i] = item[~i], item[i]
