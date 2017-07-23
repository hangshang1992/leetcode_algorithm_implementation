class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        m_low, m_high = 0,0
        for n in nums:
            m_high, m_low = max(m_low+n, m_high), m_high
        first_circle = m_high
        for n in nums:
            m_high, m_low = max(m_low+n, m_high), m_high
        return m_high - first_circle
