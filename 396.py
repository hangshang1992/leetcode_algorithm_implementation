class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = 0; n = len(A)
        for i in range(n):
            s += i*A[i]
        sumA = sum(A); m = s
        for num in A:
            s += n*num - sumA
            m = max(m, s)
        return m
