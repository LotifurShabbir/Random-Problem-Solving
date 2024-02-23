class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def firstDig(n):
            if n < 10:
                return n
            return int(str(n)[0])

        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if gcd(firstDig(nums[i]), nums[j] % 10) == 1:
                    ans += 1
        return ans
