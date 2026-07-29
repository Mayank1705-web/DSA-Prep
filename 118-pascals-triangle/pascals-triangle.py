class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if (numRows == 0):
            return []
        if (numRows == 1):
            return [[1]]
        prevRows = self.generate(numRows - 1)
        prevRow = prevRows[-1]
        currentRow = [1]

        for i in range(1, numRows - 1):
            currentRow.append(prevRow[i - 1] + prevRow[i])

        currentRow.append(1)
        prevRows.append(currentRow)

        return prevRows