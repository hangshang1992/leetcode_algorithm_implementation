class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(A)
        m = len(A[0])
        k = len(B[0])
        res = [[0 for _ in range(k)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if A[i][j] != 0:
                    for l in range(k):
                        res[i][l] += A[i][j]*B[j][l]
        return res
