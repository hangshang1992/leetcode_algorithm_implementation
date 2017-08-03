class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        index_a = len(a) - 1
        index_b = len(b) - 1
        carry = 0
        sum = ""
        while index_a >=0 or index_b >= 0 or carry:
            x = int(a[index_a]) if index_a >= 0 else 0
            y = int(b[index_b]) if index_b >= 0 else 0
            carry, val = divmod(x+y+carry,2)
            if val == 1:
                sum = '1' + sum
            else:
                sum = '0' + sum
            index_a -= 1
            index_b -= 1
        return sum
