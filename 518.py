class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        res = [0 for _ in range(amount + 1)]
        res[0] = 1
        for n in coins:
            for i in range(amount+1):
                if i>n:
                    res[i] += res[i-n]
                if i == n:
                    res[i] += 1
        return res[-1]
