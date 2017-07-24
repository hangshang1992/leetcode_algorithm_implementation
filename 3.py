class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        j = 0
        ans = 0
        dic = dict()
        for item in s:
            dic[item] = 0
        for i in range(len(s)):
            while j<len(s) and dic[s[j]] == 0:
                ans = max(ans, j-i+1)
                dic[s[j]] = 1
                j += 1
            dic[s[i]] = 0
        return ans
