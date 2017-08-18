class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, key = lambda x: (x[0], -1*x[1]), reverse= True)
        res = []
        for item in people:
            res.insert(item[1], item)
        return res
