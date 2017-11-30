def solveNQueens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    def solveNQueens(res,board,row,n):
        if row==n:
            res.append(board)
            return
        for col in range(0,n):
            if isValid(board,row,col,n):
                board[row][col]='Q'
                solveNQueens(res,board,row+1,n)
                board[row][col]='.'
    def isValid(board,row,col,n):
        for i in range(0,row):
            if board[i][col]=='Q':
                return False
        i=row-1
        j=col-1
        while i>=0 and j>=0:
            if board[i][j]=='Q':
                return False
            i-=1
            j-=1
        i=row-1
        j=col+1
        while i>=0 and j <n:
            if board[i][j]=='Q':
                return False
        return True

    board=[]
    for i in range(0,n):
        board.append([])
        for j in range(0,n):
            board[i].append('.')


