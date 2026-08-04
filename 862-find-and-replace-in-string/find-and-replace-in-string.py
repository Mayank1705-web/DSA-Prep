class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        replace = {}

        for i, src, tar in zip(indices, sources, targets):
            if s[i:i+len(src)] == src:
                replace[i] = (src, tar)

        ans = []
        i = 0

        while i < len(s):
            if i in replace:
                src, tar = replace[i]
                ans.append(tar)
                i += len(src)
            else:
                ans.append(s[i])
                i += 1

        return "".join(ans)