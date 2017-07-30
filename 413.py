class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        curr = sum1 = 0
        for i in range(2, len(A)):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                curr += 1
                sum1 += curr
            else:
                curr = 0
        return sum1
