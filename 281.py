class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.nums = []
        for i in range(min(len(v1), len(v2))):
            self.nums.append(v1.pop(0))
            self.nums.append(v2.pop(0))
        self.nums += v1 + v2

    def next(self):
        """
        :rtype: int
        """
        return self.nums.pop(0)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.nums) == 0:
            return False
        return True

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
