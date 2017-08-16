class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.nums.append(number)
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        dic = dict()
        for item in self.nums:
            if item not in dic:
                dic[value - item] = 0
            else:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
