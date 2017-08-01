class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sourceHash, targetHash, set1 = dict(), dict(), set()
        for item in s:
            set1.add(item)
            if item not in sourceHash:
                sourceHash[item] = 0
            sourceHash[item] += 1
        for item in t:
            set1.add(item)
            if item not in targetHash:
                targetHash[item] = 0
            targetHash[item] += 1
        for item in set1:
            try:
                if sourceHash[item] != targetHash[item]:
                    return False
            except:
                return False
        return True
