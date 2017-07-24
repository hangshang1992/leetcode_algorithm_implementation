class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = [item for item in s.split(" ") if item != ""]
        return 0 if len(a) ==0 else len(a[-1])
