class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sourceHash, targetHash = dict(), dict()
        for i, val in enumerate(s):
            sourceHash[val] = sourceHash.get(val, []) + [i]
        for i, val in enumerate(t):
            targetHash[val] = targetHash.get(val, []) + [i]
        return sorted(sourceHash.values()) == sorted(targetHash.values())
