class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_group(cells: list[str]) -> bool:
            seen = set()
            for cell in cells:
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)
            return True

        # Validate rows
        for row in board:
            if not is_valid_group(row):
                return False

        # Validate columns
        for j in range(9):
            col = [board[i][j] for i in range(9)]
            if not is_valid_group(col):
                return False

        # Validate 3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                cells = [
                    board[i][j]
                    for i in range(box_row, box_row + 3)
                    for j in range(box_col, box_col + 3)
                ]
                if not is_valid_group(cells):
                    return False

        return True