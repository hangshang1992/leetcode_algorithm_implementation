class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic, result = dict(), []
        for item in nums1:
            dic[item] = dic.get(item,0) + 1
        for item in nums2:
            if item in dic and dic.get(item,0) > 0:
                result.append(item)
                dic[item] -= 1
        return result
