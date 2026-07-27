class Solution(object):
    def isValidSudoku(self, board):
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                num = int(board[r][c]) - 1
                mask = 1 << num
                box = (r // 3) * 3 + (c // 3)

                if (rows[r] & mask) or (cols[c] & mask) or (boxes[box] & mask):
                    return False

                rows[r] |= mask
                cols[c] |= mask
                boxes[box] |= mask

        return True