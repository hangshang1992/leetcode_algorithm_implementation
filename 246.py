class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in range(len(num)/2 + 1):
            if not self.valid(num[i], num[~i]):
                return False
        return True
    def valid(self, left, right):
        if left == '0' and right == '0':
            return True
        elif left == '6' and right == '9':
            return True
        elif left == '1' and right == '1':
            return True
        elif left == '9' and right == '6':
            return True
        elif left == '8' and right == '8':
            return True
        return False
