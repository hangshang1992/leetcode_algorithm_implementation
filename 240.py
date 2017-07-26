class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: 
            return False
        m, n = len(matrix)-1, 0
        while m>=0 and n<len(matrix[0]):
            if matrix[m][n] == target:
                return True
            elif matrix[m][n] > target:
                m -= 1
            else:
                n += 1
        return False
