class Solution(object):
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if n <= 0:return []
        res = [[1]]
        for _ in range(n-1):
            temp = [0] + res[-1] +[0]
            res.append([temp[i]+temp[i+1] for i in range(len(temp)-1)])
        return res
