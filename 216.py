class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = range(1,10)
        res = []
        self.dfs(nums, 0, [], res, k, n)
        return res
    def dfs(self, nums, index, path, res, k, n):
        if len(path) > k:
            return
        if len(path) == k and sum(path) == n:
            res.append(path)
            return
        for i in range(index,len(nums)):
            self.dfs(nums, i + 1, path +[nums[i]], res, k, n)
