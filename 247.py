class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        hash1 = {'1':"1", '9':"6", '8':"8", '6':"9", '0':"0"}
        self.dfs(result, [None]*n, 0, n-1, hash1)
        return result
    def dfs(self, result, path, start, end, hash1):
        if start > end:
            result.append(''.join(path))
            return
        for key in hash1:
            if start == end and key in ['6', '9']:
                continue
            if start != end and start == 0 and key == '0':
                continue
            path[start] = key
            path[end] = hash1[key]
            self.dfs(result, path, start + 1, end - 1, hash1)
