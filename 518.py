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
                new_amount = i + n
                if new_amount > amount or res[i] == 0:
                    continue
                res[new_amount] += res[i]
        return res[-1]
