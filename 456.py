class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        ak, stack = -float('inf'), [nums[-1]]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < ak:
                return True
            if nums[i] > stack[-1]:
                while stack and nums[i] > stack[-1]:
                    ak = max(stack.pop(), ak)
            stack.append(nums[i])
        return False
