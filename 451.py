class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = sorted([[s.count(word), word] for word in set(s)], reverse = True)
        return ''.join([item[0]*item[1] for item in res])
