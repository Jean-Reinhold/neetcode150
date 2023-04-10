class Solution:
    """
    O(n*m)

    make a checker for each case (rows, cols and sub-boxes)

    the number count in each checker must never pass 1, so
    if a number is already in the checker, return false
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols_checker = collections.defaultdict(set)
        rows_checker = collections.defaultdict(set)
        boxes_checker = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows_checker[r]
                    or board[r][c] in cols_checker[c]
                    or board[r][c] in boxes_checker[(r // 3, c // 3)]
                ):
                    return False
                cols_checker[c].add(board[r][c])
                rows_checker[r].add(board[r][c])
                boxes_checker[(r // 3, c // 3)].add(board[r][c])

        return True