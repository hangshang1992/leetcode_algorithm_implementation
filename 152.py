class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f, g= [nums[0]], [nums[0]]
        for i in range(1, len(nums)):
            f.append(max(f[i-1]*nums[i], g[i-1]*nums[i], nums[i]))
            g.append(min(f[i-1]*nums[i], g[i-1]*nums[i], nums[i]))
        return max(f)
