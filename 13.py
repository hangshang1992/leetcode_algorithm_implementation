class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M':1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        res = 0
        p = 'I'
        for c in s[::-1]:
            res, p = res - roman[c] if roman[c] < roman[p] else res + roman[c], c
        return res
