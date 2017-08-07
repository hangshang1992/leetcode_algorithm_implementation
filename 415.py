class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        index_1 = len(num1) - 1
        index_2 = len(num2) - 1
        carry = 0
        res = ''
        while index_1 >= 0 or index_2 >= 0 or carry:
            first = int(num1[index_1]) if index_1 >= 0 else 0
            second = int(num2[index_2]) if index_2 >= 0 else 0
            carry, val = divmod(first + second + carry, 10)
            res = str(val) + res
            index_1 -= 1
            index_2 -= 1
        return res
