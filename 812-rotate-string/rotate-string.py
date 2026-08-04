class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        for i in range(len(s)):
            if s == goal:
                return True
            else:
                s = s[1:] + s[0]        
        return False
        