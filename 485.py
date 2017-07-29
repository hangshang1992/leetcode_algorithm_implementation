class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        history = 0
        for item in nums:
            if item == 1:
                count += 1
            else:
                history = max(history, count)
                count = 0
        history = max(count, history)
        return history
