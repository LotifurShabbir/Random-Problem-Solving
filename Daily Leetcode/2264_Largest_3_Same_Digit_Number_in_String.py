class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = -1
        #67778999
        for i in range(2, len(num)):
            if num[i] == num[i - 1] == num[i-2]:
                temp = num[i] + num[i - 1] + num[i - 2]
                temp = int(temp)
                ans = max(temp, ans)
        if ans == 0:
            return "000"
        elif ans == -1:
            return ""
        else:
            return str(ans)

        