class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        pos1 = -1
        pos2 = -1
        distance = float("inf")
        for i in range(len(words)):
            if words[i] == word1:
                pos1 = i
                if pos2 != -1 and pos1 - pos2 < distance:
                    distance = pos1 - pos2
            elif words[i] == word2:
                pos2 = i
                if pos1 != -1 and pos2 - pos1 < distance:
                    distance = pos2 - pos1
        return distance
