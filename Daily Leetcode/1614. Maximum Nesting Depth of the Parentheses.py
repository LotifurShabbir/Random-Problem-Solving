class Solution:
    def maxDepth(self, s: str) -> int:
        cur, res = 0, 0

        for i in s:
            if i == "(":
                cur += 1
            elif i == ")":
                cur -= 1
            res = max(res, cur)
            
        return res