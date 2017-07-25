class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:return []
        res = [1]
        for _ in range(rowIndex):
            temp = [0] + res + [0]
            res = [temp[i]+temp[i+1] for i in range(len(temp)-1)]
        return res
