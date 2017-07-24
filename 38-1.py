class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n<=0: return ""
        res = "1"
        for i in range(n-1):
            res = ''.join([str(len(list(group))) + digit for digit, group in itertools.groupby(res)])
        return res
