class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        board = ["."*n for _ in range(n)]
        leftrow = [0]*n
        upperDiagonal = [0]*(2*n-1)
        lowerDiagonal = [0]*(2*n-1)
        self.func(0,board,res,n,leftrow,upperDiagonal,lowerDiagonal)
        return len(res)

    def func(self,col,board,res,n,leftrow,upperDiagonal,lowerDiagonal):
        if col == n:
            res.append(board[:])
            return

        for row in range(n):
           if(
            leftrow[row] == 0
            and upperDiagonal[n-1+col-row] == 0
            and lowerDiagonal[row + col] == 0
           ):
            board[row] =board[row][:col] + "Q" + board[row][col+1:]
            leftrow[row] = 1
            upperDiagonal[n-1+col-row] = 1
            lowerDiagonal[row+col] = 1

            self.func(col+1,board,res,n,leftrow,upperDiagonal,lowerDiagonal)

            board[row] = board[row][:col] + "." + board[row][col+1:]
            leftrow[row] = 0
            upperDiagonal[n-1+col-row] = 0
            lowerDiagonal[row+col] = 0
        