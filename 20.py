class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = []
        for item in s:
            if item == "{" or item == "(" or item == "[":
                result.append(item)
            else:
                try:
                    temp = result.pop()
                    if (item == "}" and temp == "{") or (item == ")" and temp == "(") or (item == "]" and temp == "["):
                        continue
                    else:
                        return False
                except:
                    return False
        if result != []:
            return False
        return True
