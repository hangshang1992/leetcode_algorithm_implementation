class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        res = []
        for item in triangle[::-1]:
            if res == []:
                res = item
                continue
            for j in range(len(item)):
                item[j] = min(item[j] + res[j], item[j] + res[j+1])
            res = item
        return res[-1]
