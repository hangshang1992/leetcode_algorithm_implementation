class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums[:] = self.divide(nums)
        return nums[::-1][k-1]
    def divide(self, nums):
        length = len(nums)
        if length == 0 or length == 1:
            return nums
        left = self.divide(nums[:length//2] if length%2==0 else nums[:length//2+1])
        right = self.divide(nums[length//2:] if length%2 == 0 else nums[length//2+1:])
        return self.merge(left, right)
    def merge(self, left, right):
        l, r, result = 0, 0, []
        while l<len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        return result + left[l:] + right[r:]
