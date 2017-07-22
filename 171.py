class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter, product, result = [chr(item) for item in range(ord("A"),ord("Z")+1)], 1, 0
        for item in s[::-1]:
            result += (letter.index(item) + 1)*product
            product *= 26
        return result
