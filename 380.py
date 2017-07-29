class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mySet = set()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.mySet:
            self.mySet.add(val)
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        try:
            self.mySet.remove(val)
            return True
        except:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.sample(list(self.mySet),1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
