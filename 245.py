class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        p1 = -1
        p2 = -1
        ans = float("inf")
        same = word1 == word2
        for i in range(len(words)):
            if words[i] == word1:
                p1 = i
                if p2 != -1 and p1 - p2 < ans:
                    ans = p1 - p2
                if same:
                    p2 = p1
            elif not same and word2 == words[i]:
                p2 = i
                if p1 != -1 and p2 - p1 < ans:
                    ans = p2 - p1
        return ans
