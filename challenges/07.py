

from typing import List


class Solution:

    
    def isValidSudoku(self, board: List[List[str]]) -> bool:    
        
        columns = [[] for _ in range(len(board))]
        lenBoard = len(board)
        
        for c in range(0, lenBoard):
            
            vertical = []
            
            for i in range(0, len(board[c])):
                value = board[c][i]
                if value != ".":
                    columns[i].append(board[c][i])
                    vertical.append(value)
                    
            lenVerticalClean = len(vertical)
                    
            if len(set(vertical)) != lenVerticalClean:
                return False
            
            
            if c + 1 == lenBoard:
                for i in columns:
                    if len(i) != len(set(i)):
                        return False
            
            if c != 0 and c + 1 % 3 == 0:
                square = [[] for _ in range(3)]
                index = 0
                for i in range(0, 3):
                    for h in range(0, len(board)):
                        value = board[c - i][h]
                        if value != ".":
                            square[index].append(value)
                        if h != 0 and h + 1 % 3 == 0:
                            index += 1
                    index = 0
                    
                for i in square:
                    lenSquareClean = len(i)
                    if len(set(i)) != lenSquareClean:
                        return False
                
                
            
        return True
                
            
                    
var = Solution()

print(var.isValidSudoku([[".",".","4",".",".",".","6","3","."],
                         [".",".",".",".",".",".",".",".","."],
                         ["5",".",".",".",".",".",".","9","."],
                         [".",".",".","5","6",".",".",".","."],
                         ["4",".","3",".",".",".",".",".","1"],
                         [".",".",".","7",".",".",".",".","."],
                         [".",".",".","5",".",".",".",".","."],
                         [".",".",".",".",".",".",".",".","."],
                         [".",".",".",".",".",".",".",".","."]]))
                
                
            
        