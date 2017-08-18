class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        wordSet = set()
        for item in bank:
            wordSet.add(item)
        queue = collections.deque([(start, 0)])
        while queue:
            currGen, currLen = queue.popleft()
            if currGen == end:
                return currLen
            for i in range(8):
                part1 = currGen[:i]
                part2 = currGen[i+1:]
                for j in 'ACGT':
                    nextGen = part1 + j + part2
                    if nextGen in wordSet:
                        queue.append((nextGen, currLen + 1))
                        wordSet.remove(nextGen)
        return -1
