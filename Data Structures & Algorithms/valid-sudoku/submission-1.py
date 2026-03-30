class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i, row in enumerate(board):
            for j, c in enumerate(row):
                box = 0
                if c == ".": continue
                if i > 2: box += 1
                if j > 2: box += 3
                if i > 5: box += 1
                if j > 5: box += 3
                if c in rows[i]: return False
                if c in cols[j]: return False
                if box > 8:
                    print(f"FAIL: {i=} {j=} {box=} {c=}")

                if c in boxes[box]:
                    print(f"FAIL: {i=} {j=} {box=} {c=} {boxes[box]=}")
                    return False
                rows[i].add(c)
                cols[j].add(c)
                boxes[box].add(c)
                print(f"{i=} {j=} {box=} {c=} {rows[i]=} {cols[j]=} {boxes[box]=}")
        
        return True