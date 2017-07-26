class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count1, count2, majority1, majority2 = 0, 0, "", ""
        for item in nums:
            if count1 > 0 and majority1 == item:
                count1 += 1
                continue
            if count2 > 0 and majority2 == item:
                count2 += 1
                continue
            if count1 == 0:
                majority1 = item
                count1 += 1
                continue
            if count2 == 0:
                majority2 = item
                count2 += 1
                continue
            count1 -= 1
            count2 -= 1
        result = []
        for item in [majority1, majority2]:
            count = 0
            for item1 in nums:
                if item == item1:
                    count += 1
            if count > len(nums)/3 and item not in result:
                result.append(item)
        return result
