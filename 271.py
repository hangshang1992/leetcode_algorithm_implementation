class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        elif strs == [""]:
            return '-'
        else:
            return 'x01|'.join(strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        if s == '':
            return []
        elif s == '-':
            return [""]
        else:
            return s.split("x01|")

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
