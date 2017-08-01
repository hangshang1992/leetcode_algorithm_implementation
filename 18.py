class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        res = []
        length = len(nums)
        for i in range(length - 3):
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, length - 2):
                if j != i+1 and nums[j-1] == nums[j]:
                    continue
                sum1 = target - nums[i] - nums[j]
                l, r = j+1, length -1
                while l< r:
                    total = nums[l] + nums[r]
                    if total == sum1:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l<r and nums[l] == nums[l+1]:
                            l += 1
                        while l<r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif total > sum1:
                        r -= 1
                    else:
                        l += 1
        return res
