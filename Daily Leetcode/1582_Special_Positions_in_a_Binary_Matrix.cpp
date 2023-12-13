class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans, row_size, col_size = 0, len(mat), len(mat[0])
        for row in range(row_size):
            for col in range(col_size):
                if mat[row][col] == 0:
                    continue
                check = True
                #col checking
                for r in range(row_size):
                    if r != row and mat[r][col] == 1:
                        check = False
                        break
                #row checking
                for c in range(col_size):
                    if c != col and mat[row][c] == 1:
                        check = False
                        break
                if(check):
                    ans += 1
        return ans
        