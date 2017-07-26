class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        start, end = 0, len(matrix) - 1
        while start + 1 < end:
            middle = (end - start)/2 + start
            if matrix[middle][0] == target:
                return True
            if matrix[middle][0] > target:
                end = middle
            else:
                start = middle
        if matrix[start][0] == target or matrix[end][0] == target:
            return True
        elif matrix[start][0] > target:
            row = start - 1
        elif matrix[start][0] < target and matrix[end][0] > target:
            row = start
        else:
            row = end
        start, end = 0, len(matrix[0]) - 1
        while start + 1 < end:
            middle = (end - start)/2 + start
            if matrix[row][middle] == target:
                return True
            if matrix[row][middle] > target:
                end = middle
            else:
                start = middle
        if matrix[row][start] == target or matrix[row][end] == target:
            return True
        else:
            return False
