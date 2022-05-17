class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowT = [dict() for _ in range(9)]
        colT = [dict() for _ in range(9)]
        boxT = [dict() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                num = board[i][j]
                rowT[i][num] = rowT[i].get(num, 0) + 1
                colT[j][num] = colT[j].get(num, 0) + 1
                boxT[i // 3 * 3 + j // 3][num] = boxT[i // 3 * 3 + j // 3].get(num, 0) + 1
                
                if rowT[i][num] > 1 or colT[j][num] > 1 or boxT[i // 3 * 3 + j // 3][num] > 1:
                    return False
        return True
                
