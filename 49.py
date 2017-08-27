class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = dict()
        for item in strs:
            temp = ''.join(sorted(item))
            dic[temp] = dic.get(temp, []) + [item]
        return dic.values()
