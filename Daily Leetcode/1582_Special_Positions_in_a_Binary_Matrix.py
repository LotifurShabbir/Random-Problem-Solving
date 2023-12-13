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
# // little bit optimized
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rl = len(mat)
        cl = len(mat[0])
        ans = 0

        rowsum = []
        colsum = []
        row = 0
        while row != rl:
            temp = 0
            for col in range(cl):
                temp += mat[row][col]
            rowsum.append(temp)
            temp = 0
            row += 1
        col = 0
        while col != cl:
            temp = 0
            for row in range(rl):
                temp += mat[row][col]
            colsum.append(temp)
            temp = 0
            col += 1
        for row in range(rl):
            for col in range(cl):
                if mat[row][col] == 1 and rowsum[row] == 1 and colsum[col] == 1:
                    ans += 1
        return ans

        