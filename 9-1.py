class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = str(x)
        for i in range(len(a)/2):
            if a[i] != a[~i]:
                return False
        return True
