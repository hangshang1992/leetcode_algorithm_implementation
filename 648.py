class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        nums = sentence.split(" ")
        for i in range(len(nums)):
            for item in dict:
                if item == nums[i][:len(item)]:
                    nums[i] = item
                    break
        return ' '.join(nums)
