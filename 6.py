class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows<2 or len(s)<numRows: return s
        rows = [""]*numRows
        ind, step = 0, 1
        for v in s:
            rows[ind] += v
            if ind == 0: step = 1
            elif ind == numRows-1: step = -1
            ind += step
        return ''.join(rows)
