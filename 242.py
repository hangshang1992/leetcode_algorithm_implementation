class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sourceHash, targetHash = dict(), dict()
        set1 = set()
        for item in s:
            set1.add(item)
            sourceHash[item] = sourceHash.get(item, 0) + 1
        for item in t:
            set1.add(item)
            targetHash[item] = targetHash.get(item, 0) + 1
        for item in set1:
            try:
                if targetHash[item] != sourceHash[item]:
                    return False
            except:
                return False
        return True
