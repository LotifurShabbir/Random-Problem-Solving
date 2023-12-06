class Solution:
    def totalMoney(self, n: int) -> int:
        day = 0
        add = 1 #first week
        final_ans = 0

        while day < n:
            final_ans += add
            add += 1
            day += 1

            if day % 7 == 0:
                add = day // 7 + 1

        return final_ans
        

        