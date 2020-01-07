class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums_set = set()
        while n != 1:
            num_sum = 0
            while n > 0:
                tmp = n % 10
                num_sum += tmp ** 2
                n /= 10
            if num_sum in nums_set:
                return False
            else:
                nums_set.add(num_sum)
            n = num_sum
        return True
