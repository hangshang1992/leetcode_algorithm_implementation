class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num:
            return True
        l, r = 0, len(num) - 1
        while l <= r:
            if not self.isGrammatic(num[l], num[r]):
                return False
            l += 1
            r -= 1
        return True
    def isGrammatic(self, l, r):
        if l == "0" and r == "0":
            return True
        elif l == '1' and r == '1':
            return True
        elif l == "8" and r == "8":
            return True
        elif l == "6" and r == "9":
            return True
        elif l == "9" and r == "6":
            return True
        else:
            return False
