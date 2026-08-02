class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        ans = ""

        for i in s:
            if i.isalnum():
                ans += i
        i = 0
        j = len(ans) -1
        while i < j: 
            if ans[i] == ans[j]:
                i += 1
                j -= 1
            else:
                return False

        return True
        