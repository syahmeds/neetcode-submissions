class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Iterate over every item in each row
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[0])):
                current_item = board[i][j]
                if not current_item == ".":
                    if current_item in seen:
                        return False
                    else:
                        seen.add(current_item)
    
        # Iterate over every item in each column
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[0])):
                current_item = board[j][i]
                if not current_item == ".":
                    if current_item in seen:
                        return False
                    else:
                        seen.add(current_item)

        # Iterate over every item in each internal 3x3 grid:
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                seen = set()
                for i in range(box_row, box_row+3):
                    for j in range(box_col,box_col+3):
                        current_item = board[i][j]
                        if not current_item == ".":
                            if current_item in seen:
                                return False
                            else:
                                seen.add(current_item)
    
        return True