class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s: return ""
        minStr = ""
        targetHash, sourceHash = dict(), dict()
        for item in t:
            if item not in targetHash:
                targetHash[item] = 0
            targetHash[item] += 1
        for item in s:
            sourceHash[item] = 0
        j = 0
        ans = float("inf")
        for i in range(len(s)):
            while not self.valid(sourceHash, targetHash) and j<len(s):
                sourceHash[s[j]] += 1
                j += 1
            if self.valid(sourceHash, targetHash) and ans > j-i :
                ans = min(ans, j-i)
                minStr = s[i:j]
            sourceHash[s[i]] -= 1
        return minStr
                
    def valid(self, sourceHash, targetHash):
        for item in targetHash:
            try:
                if targetHash[item] > sourceHash[item]:
                    return False
            except:
                return
