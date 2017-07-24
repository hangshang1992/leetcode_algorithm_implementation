class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(n)] for _ in range(n)]
        i,di,j,dj = 0,0,0,1
        for value in range(1,n**2+1):
            res[i][j] = value
            if res[(i+di)%n][(j+dj)%n] !=0:
                di, dj = dj,-di
            i +=di
            j += dj
        return res
