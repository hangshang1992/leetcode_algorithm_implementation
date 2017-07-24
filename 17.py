class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        self.dfs(digits, dic, 0, "", res)
        return res
    def dfs(self, digits, dic, index, path, res):
        if len(digits) == len(path):
            res.append(path)
            return
        for item in dic[digits[index]]:
            self.dfs(digits, dic, index + 1, path + item, res)
