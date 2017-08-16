class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        length = len(s)
        if length <= 10:
            return []
        right = 10
        dic = dict()
        res = []
        for left in range(length - 9):
            dic[s[left:right]] = dic.get(s[left:right], 0) + 1
            if dic[s[left:right]] >= 2 and s[left:right] not in res:
                res.append(s[left:right])
            right += 1
        return res
