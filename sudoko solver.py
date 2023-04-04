class Solution:
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        row = { i:[0]*10 for i in range(0,9) }
        col = { i:[0]*10 for i in range(0,9) }
        box = { i:[0]*10 for i in range(0,9) }
        n,m = len(board),len(board[0])
        for i in range(0,n):
            for j in range(0,m):
                box_index = 3*(i//3) + j//3 
                c = ord(board[i][j][0]) - ord('0')
                if( c < 0 or c > 9 ):
                    board[i][j] = 0
                else: 
                    board[i][j] = c ;
                    row[i][c] = 1
                    col[j][c] = 1
                    box[box_index][c] = 1

        
        def rec(i,j):
            if( board[i][j] > 0 and board[i][j] <= 9  ):
                if( j < 8 ):
                    if( rec(i,j+1)):
                        return True
                elif( i < 8 ):
                    if( rec(i+1,0) ):
                        return True 
                elif( i == 8 and j == 8 ):
                    return True ;
            else:
                box_index = 3*(i//3) + j//3   
                for k in range(1,10):
                    if( row[i][k] == col[j][k] == box[box_index][k] == 0 ):
                        row[i][k] = col[j][k] = box[box_index][k] = 1
                        board[i][j] = k 
                        if( j < 8 ):
                            if(rec(i,j+1)):
                                return True;
                        elif( i < 8 ):
                            if( rec(i+1,0) ):
                                return True ;
                        else:
                            return True;
                        board[i][j] = 0 
                        row[i][k] = col[j][k] = box[box_index][k] = 0
                
            return False;
        
        rec(0,0)

        
        for i in range(0,9):
            for j in range(0,9):
                board[i][j] = chr(board[i][j]+ord('0'))


        return board;

        