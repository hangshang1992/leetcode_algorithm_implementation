class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = 0, 0
        while n < len(t):
            if m > len(s) -1:
                break
            if t[n] == s[m]:
                m += 1
            n += 1
        return m == len(s)
