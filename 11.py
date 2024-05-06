class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        left = 0
        right = len(height) - 1
        while right > left:
            area = max(area, (right - left ) * min(height[left], height[right]))
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return area
