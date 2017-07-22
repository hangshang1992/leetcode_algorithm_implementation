class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, majority = 1, nums[0]
        for item in nums[1:]:
            if majority!=item:
                if count ==0:
                    count = 1
                    majority = item
                else:
                    count -= 1
            else:
                count += 1
        return majority
