class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.dic = dict()
        for i in range(len(words)):
            self.dic[words[i]] = self.dic.get(words[i], []) + [i]

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        temp1, temp2 = self.dic[word1], self.dic[word2]
        m, n, i, j, res = len(temp1), len(temp2), 0, 0, float("inf")
        while i < m and j < n:
            res = min(res, abs(temp1[i] - temp2[j]))
            if temp1[i] < temp2[j]:
                i += 1
            else:
                j += 1
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
