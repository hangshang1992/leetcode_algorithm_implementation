class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        m_low, m_high, m_low1, m_high1 = 0,0,0,0
        for n in nums[1:]:
            m_high, m_low = max(n + m_low, m_high), m_high
        for n in nums[:-1]:
            m_high1, m_low1 = max(n+m_low1, m_high1), m_high1
        return max(m_high, m_high1)
        
