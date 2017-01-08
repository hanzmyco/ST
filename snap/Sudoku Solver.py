def solve(board, row):
    for i in xrange(row, 9):
        for j in xrange(0, 9):
            if board[i][j] != '.':
                continue
            for k in xrange(1, 10):
                board[i][j] = str(k)
                if  isValid(board, i, j):
                    if j < 8:
                        if  solve(board, i):
                            return True
                    elif j == 8 and i < 8:
                        if  solve(board, i + 1):
                            return True
                    elif j == 8 and i == 8:  # the end

                        print board
                        return True
                board[i][j] = '.'

            return False
    return True  # everything else is full now


def isValid(  board, a, b):
    num = board[a][b]
    for i in xrange(0, 9):
        if i != a and num == board[i][b]:
            return False
    for j in xrange(0, 9):
        if j != b and num == board[a][j]:
            return False
    begin_row = a / 3 * 3
    begin_col = b / 3 * 3
    for k in xrange(0, 9):
        x = begin_row + k / 3
        y = begin_col + k % 3
        if (x != a or y != b) and board[x][y] == num:
            return False
    return True


def solveSudoku( ):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    board=[[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    solve(board, 0)

solveSudoku()