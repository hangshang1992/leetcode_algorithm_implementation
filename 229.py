class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        x = [float('inf'),float('inf')]
        cnt = [0,0]
        length = len(nums)
        for i in range(length):
            if cnt[0] > 0 and x[0] == nums[i]:
                cnt[0] += 1
                continue
            if cnt[1] > 0 and x[1] == nums[i]:
                cnt[1] += 1
                continue
            if cnt[0] == 0:
                x[0] = nums[i]
                cnt[0] = 1
                continue
            if cnt[1] == 0:
                x[1] = nums[i]
                cnt[1] = 1
                continue
            cnt[0] -= 1
            cnt[1] -= 1
        for i in range(2):
            if cnt[i] > 0:
                count = 0
                for item in nums:
                    if x[i] == item:
                        count += 1
                if count > length/3:
                    result.append(x[i])
        return result
