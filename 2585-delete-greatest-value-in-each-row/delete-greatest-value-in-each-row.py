class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        while any(grid):
            count += max(max(row) for row in grid if row)
            for row in grid:
                if row:
                    row.remove(max(row))
        return count