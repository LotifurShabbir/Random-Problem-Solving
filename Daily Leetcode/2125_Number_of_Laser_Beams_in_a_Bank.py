class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev_one = 0

        for i in bank:
            one_count = i.count('1')
            if one_count == 0:
                continue
            ans += one_count * prev_one
            prev_one = one_count

        return ans
