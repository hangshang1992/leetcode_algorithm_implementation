class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic = dict()
        for s in strings:
            temp = '-'.join(map(str,[(ord(item)-ord(s[0]))%26 for item in s]))
            dic[temp] = dic.get(temp,[]) + [s]
        return [sorted(x) for x in dic.values()]
