class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        res = [0,0]
        for item in moves:
            if item == "U":
                res[0] += 1
            elif item == "D":
                res[0] -= 1
            elif item == "L":
                res[1] +=1
            else:
                res[1] -= 1
        return res == [0,0]
