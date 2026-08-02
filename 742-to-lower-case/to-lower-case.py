class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Using in build fubction
        # return s.lower()
        result = ""
        for ch in s:
            if 65 <= ord(ch) <= 90:
                result += chr(ord(ch) + 32)
            else:
                result += ch
        return result