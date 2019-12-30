class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def kadane(num):
            max_end = num[0]
            max_so_far = num[0]
            for i in range(1, len(num)):
                max_end = max(num[i], max_end + num[i])
                max_so_far = max(max_so_far, max_end)
            return max_so_far
        
        if max(A) < 0:
            return max(A)
        res1 = kadane(A)
        
        res2 = sum(A) + kadane([-num1 for num1 in A])
        # print res1
        return max(res1, res2)
        
