class Solution(object):
    def solveSudoku(self, board):
        self.board=board
        self.row = [[0 for i in range(9)] for j in range(9)]
        self.col=[[0 for i in range(9)] for j in range(9)]
        self.box=[[0 for i in range(9)] for j in range(9)]
        for r in range(9):
            for c in range(9):
                if(board[r][c]!=0):
                    self.row[r][board[r][c]-1]=self.col[c][board[r][c]-1]=self.box[3*(r//3)+(c//3)][board[r][c]-1]=1
        flag=self.solve(0,0)
        return flag,self.board
    def solve(self,i,j):
        if i==9:
            return True
        if j==9:
            return self.solve(i+1,0)
        if(self.board[i][j]!=0):
            return self.solve(i,j+1)
        for c in range(1,10):
            if(self.row[i][c-1]==0 and self.col[j][c-1]==0 and self.box[3 * (i//3) +(j//3)][c-1]==0):
                self.board[i][j]=c
                self.row[i][c-1]=1
                self.col[j][c-1]=1
                self.box[3 * (i//3) +(j//3)][c-1]=1
                if(self.solve(i,j+1)):
                    return True
                self.board[i][j]=0
                self.row[i][c-1]=0
                self.col[j][c-1]=0
                self.box[3* (i//3) +(j//3)][c-1]=0      
        return False
def solve_sudoku(board):
    s_instance=Solution()
    solvable,board=s_instance.solveSudoku(board)
    return solvable,board

			
