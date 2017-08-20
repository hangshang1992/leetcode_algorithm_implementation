class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = dict()
        res = []
        for i in range(len(s)-9):
            if s[i:i+10] in dic and s[i:i+10] not in res:
                res.append(s[i:i+10])
            else:
                dic[s[i:i+10]] = 0
        return res
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        set1 = set()
        res = []
        for i in range(len(s)-9):
            if s[i:i+10] in set1 and s[i:i+10] not in res:
                res.append(s[i:i+10])
            else:
                set1.add(s[i:i+10])
        return res
