class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s== "" or s[0] == "0": 
            return 0
        res = [0 for _ in range(len(s)+1)]
        res[0] = 1
        res[1] = 1
        for i in range(2, len(s)+1):
            if int(s[i-2:i])>10 and int(s[i-2:i])<=26 and s[i-1]!='0':
                res[i] = res[i-1] + res[i-2]
            elif s[i-2:i] == '10' or s[i-2:i] == '20':
                res[i] = res[i-2]
            elif s[i-1]!='0':
                res[i] = res[i-1]
            else:
                return 0
        return res[-1]
