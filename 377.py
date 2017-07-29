class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = [1] + [0 for _ in range(target)]
        for i in range(target+1):
            for n in nums:
                if i >= n:
                    result[i] += result[i-n]
        return result[-1]
