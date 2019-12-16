class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        result = []
        length1 = len(word1) + 1
        length2 = len(word2) + 1
        for i in range(length1):
            tmp_result = [0]  * length2
            result.append(tmp_result)
        for i in range(length1):
            result[i][0] = i
        for j in range(1, length2):
            result[0][j] = j
        for i in range(1, length1):
            for j in range(1, length2):
                if word1[i-1] == word2[j-1]:
                    result[i][j] = result[i-1][j-1]
                else:
                    result[i][j] = min(result[i-1][j-1], result[i-1][j], result[i][j-1]) + 1
        return result[-1][-1]
