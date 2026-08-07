class Solution(object):
    def arrayRankTransform(self, arr):
        rank = sorted(set(arr))

        mp = {}
        for i in range(len(rank)):
            mp[rank[i]] = i + 1

        result = []
        for x in arr:
            result.append(mp[x])

        return result