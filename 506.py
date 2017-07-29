class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        temp = sorted(nums,reverse=True)
        for i in range(len(temp)):
            if i == 0:
                nums[(nums.index(temp[i]))] = "Gold Medal"
            elif i == 1:
                nums[(nums.index(temp[i]))] = "Silver Medal"
            elif i == 2:
                nums[(nums.index(temp[i]))] = "Bronze Medal"
            else:
                nums[(nums.index(temp[i]))] = str(i+1)
        return nums
