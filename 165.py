class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = map(int,version1.split("."))
        v2 = map(int, version2.split("."))
        length = len(v2) - len(v1)
        return cmp(v1+[0]*length,v2+[0]*-length)
