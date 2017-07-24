class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n<=0: return ""
        res = "1"
        for i in range(n-1):
            new_res = ""
            count = 0
            temp = res[0]
            for item in res:
                if temp == item:
                    count += 1
                else:
                    new_res += str(count) + temp
                    temp = item
                    count = 1
            new_res += str(count) + temp
            res = new_res
        return res
