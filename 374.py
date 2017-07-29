# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start + 1 < end:
            middle = (end - start)/2 + start
            if guess(middle) == 0:
                return middle
            elif guess(middle) == 1:
                start = middle
            else:
                end = middle
        if guess(start) == 0:
            return start
        return end
