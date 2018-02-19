class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = ['']
        for item in S:
            if item.isalpha():
                res = [i + j for i in res for j in [item.lower(), item.upper()]]
            else:
                res = [item1 + item for item1 in res]
        return res
