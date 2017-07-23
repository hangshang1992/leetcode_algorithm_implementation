class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        a = '{0:032b}'.format(n)
        rever = a[::-1]
        return int(rever,2)
