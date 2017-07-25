class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = sorted([str(item) for item in nums])
        nums.sort(cmp = lambda x,y: cmp(y+x,x+y))
        return ''.join(nums).lstrip('0') or '0'
