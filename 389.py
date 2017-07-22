class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a = 0
        for item in s:
            a ^= ord(item)
        for item in t:
            a ^= ord(item)
        return chr(a)
