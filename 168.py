class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        letter_map = [chr(item) for item in range(ord('A'), ord('Z')+1)]
        res = []
        while n > 0:
            n, val = divmod(n-1,26)
            res.append(letter_map[val])
        return ''.join(res[::-1])
