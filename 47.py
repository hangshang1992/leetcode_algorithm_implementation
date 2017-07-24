class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
        res = [[]]
        for n in nums:
            length = len(res[-1])
            new_res = []
            for item in res:
                for j in range(length,-1,-1):
                    if j<length and item[j] == n:
                        break
                    new_res.append(item[:j] + [n] + item[j:])
            res = new_res
        return res
    
