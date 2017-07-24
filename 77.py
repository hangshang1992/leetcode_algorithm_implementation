class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 1:
            return [[i] for i in range(1,n+1)]
        elif k == n:
            return [[i for i in range(1,n+1)]]
        else:
            res = []
            res += self.combine(n-1, k)
            part = self.combine(n-1,k-1)
            for item in part:
                item.append(n)
            res += part
            return res
