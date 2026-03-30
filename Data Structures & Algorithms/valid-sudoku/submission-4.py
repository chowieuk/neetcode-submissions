# Brute Force
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # each row contains no duplicates
        # each column contains no duplicates
        # each 3 x 3 sub-box contains no duplicates

        seenRows = [set() for i in range(10)]
        seenCols = [set() for i in range(10)]
        seenBoxes = [set() for i in range(10)]
        for i in range(9):
            for j in range(9):
                k = (i // 3) * 3 + (j // 3)
                val = board[i][j]
                if val != ".":
                    if val in seenRows[i] or val in seenCols[j] or val in seenBoxes[k]:
                        return False
                seenRows[i].add(val)
                seenCols[j].add(val)
                seenBoxes[k].add(val)

        return True