class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_map = str.split(" ")
        pattern_map = list(pattern)
        if len(str_map) != len(pattern_map):
            return False
        strHash, patternHash = dict(), dict()
        for i, item in enumerate(str_map):
            strHash[item] = strHash.get(item, []) + [i]
        for i, item in enumerate(pattern_map):
            patternHash[item] = patternHash.get(item, []) + [i]
        return sorted(patternHash.values()) == sorted(strHash.values())
