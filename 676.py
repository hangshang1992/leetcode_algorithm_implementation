class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set1 = set()

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for item in dict:
            self.set1.add(item)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for i in range(len(word)):
            for j in 'abcdefghijklkmnopqrstuvwsxyz':
                if j != word[i]:
                    nextword = word[:i] + j + word[i+1:]
                    if nextword in self.set1:
                        return True
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
