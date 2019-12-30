class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        current_char = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if current_char != "":
                    res.append(current_char)
                    current_char = ""
            else:
                current_char = s[i] + current_char 
        if current_char != "":
            res.append(current_char)
        return ' '.join(res)
