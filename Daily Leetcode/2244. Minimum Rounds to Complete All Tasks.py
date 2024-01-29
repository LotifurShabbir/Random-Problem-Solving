class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        if len(tasks) == 1:
            return -1
        dic = Counter(tasks)
        ans = 0
        # print(dic)
        for key, values in dic.items():
            if values < 2:
                return - 1
            elif values % 3 == 0:
                ans += values // 3
            elif values % 3 != 0:
                ans += values // 3 + 1
            elif values % 2 == 0:
                ans += 1
                
        return ans