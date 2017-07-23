class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s, [], res)
        return res
    def dfs(self, s, path, res):
        if s== "":
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPara(s[:i]):
                self.dfs(s[i:] , path + [s[:i]], res)
    def isPara(self, s):
        return s == s[::-1]
