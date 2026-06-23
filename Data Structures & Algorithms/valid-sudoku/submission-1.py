class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 3-pass
        # Iterate over every item in each row
        # for i in range(len(board)):
        #     seen = set()
        #     for j in range(len(board[0])):
        #         current_item = board[i][j]
        #         if not current_item == ".":
        #             if current_item in seen:
        #                 return False
        #             else:
        #                 seen.add(current_item)
    
        # # Iterate over every item in each column
        # for i in range(len(board)):
        #     seen = set()
        #     for j in range(len(board[0])):
        #         current_item = board[j][i]
        #         if not current_item == ".":
        #             if current_item in seen:
        #                 return False
        #             else:
        #                 seen.add(current_item)

        # # Iterate over every item in each internal 3x3 grid:
        # for box_row in range(0,9,3):
        #     for box_col in range(0,9,3):
        #         seen = set()
        #         for i in range(box_row, box_row+3):
        #             for j in range(box_col,box_col+3):
        #                 current_item = board[i][j]
        #                 if not current_item == ".":
        #                     if current_item in seen:
        #                         return False
        #                     else:
        #                         seen.add(current_item)
    
        # return True

        # 1-pass
        row_sets = [set() for _ in range(9)]

        column_sets = [set() for _ in range(9)]

        subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                current_item = board[r][c]
                if current_item == ".":
                    continue
                if current_item in row_sets[r]:
                    return False
                if current_item in column_sets[c]:
                    return False
                if current_item in subgrid_sets[r // 3][c // 3]:
                    return False

                row_sets[r].add(current_item)

                column_sets[c].add(current_item)

                subgrid_sets[r // 3][c // 3].add(current_item)

        return True