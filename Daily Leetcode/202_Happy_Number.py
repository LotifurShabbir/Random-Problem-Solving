class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        # if n < 10:
        #     return False
        temp = n
        limit = 0
        maxlimit = 10000
        while temp != 1 and limit < maxlimit:
            digsum = 0
            strtemp = str(temp)
            for i in strtemp:
                digsum += int(i) * int(i)
            temp = digsum
            limit += 1
        if temp == 1:
            return True
        else:
            return False