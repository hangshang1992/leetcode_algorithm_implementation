class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.matrix = []
        for item in vec2d:
            self.matrix += item

    def next(self):
        """
        :rtype: int
        """
        return self.matrix.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.matrix) == 0:
            return False
        return True

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
