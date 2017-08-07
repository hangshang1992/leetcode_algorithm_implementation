class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.nums = []
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.nums.append(val)
        k = self.size
        return sum(self.nums)*1.0/len(self.nums) if len(self.nums) < k else sum(self.nums[-k:])*1.0/k


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
