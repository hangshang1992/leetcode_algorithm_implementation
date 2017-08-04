class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        result = []
        for word in words:
            lower_case = set(word.lower())
            for item in [row1, row2, row3]:
                if lower_case & item == lower_case:
                    result.append(word)
                    break
        return result
