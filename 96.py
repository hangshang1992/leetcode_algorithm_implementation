class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        max_number = 2**31 - 1
        if divisor == 0: return max_number
        label = (dividend>0 and divisor<0) or (dividend < 0 and divisor > 0)
        shift = 31
        ans = 0
        a, b = abs(dividend), abs(divisor)
        while shift >= 0:
            if a>= (b<<shift):
                a -= b<<shift
                ans += 1<<shift
            shift -= 1
        if label:
            ans = -ans
        if ans > max_number:
            return max_number
        return ans
