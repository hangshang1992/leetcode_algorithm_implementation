class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        res = [[''] * 3 for _ in range(3)]
        def check(char, i, j):
            res[i][j] = char
            if res[0][0] == char and res[1][1] == char and res[2][2] == char:
                return True
            if res[2][0] == char and res[1][1] == char and res[0][2] == char:
                return True
            if res[i][0] == char and res[i][1] == char and res[i][2] == char:
                return True
            if res[0][j] == char and res[1][j] == char and res[2][j] == char:
                return True
            return False
        
        for i in range(len(moves)):
            if i % 2 == 0:
                flag = check('A', moves[i][0], moves[i][1])
                if flag:
                    return 'A'
            else:
                flag = check('B', moves[i][0], moves[i][1])
                if flag:
                    return 'B'
        return "Draw" if len(moves) == 9 else 'Pending'
