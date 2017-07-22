class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        for i in range(len(numbers)):
            if numbers[i] not in dic:
                dic[target-numbers[i]] = i
            else:
                return [dic[numbers[i]] + 1, i+1]
