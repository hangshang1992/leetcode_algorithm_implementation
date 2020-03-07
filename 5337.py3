class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        memo = {0:0}
        tmp = {a:b for a, b in zip('aeiou', range(5))}
        cur = 0
        res = 0
        for i, c in enumerate(s, 1):
            if c in tmp:
                cur ^= 1 << tmp[c]
            if cur in memo:
                res = max(res, i - memo[cur])
            else:
                memo[cur] = i
        return res
