class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates: return []
        res = []
        self.dfs(candidates, target, 0, [], res)
        return res
    def dfs(self,candidates, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(candidates)):
            self.dfs(candidates, target- candidates[i], i, path + [candidates[i]], res)
