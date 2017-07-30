class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        strs = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        ret = ""
        for i in range(len(nums)):
            while num >= nums[i]:
                ret += strs[i]
                num -= nums[i]
            if num == 0:
                return ret
