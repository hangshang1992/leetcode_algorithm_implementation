class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fac = [1]
        for i in range(1,n+1):
            fac.append(fac[-1]*i)
        elegible = range(1,n+1)
        per = []
        for i in range(1, n+1):
            digit, k = divmod(k-1, fac[n-i])
            k += 1
            per.append(elegible[digit])
            elegible.remove(elegible[digit])
        return ''.join(map(str, per))
