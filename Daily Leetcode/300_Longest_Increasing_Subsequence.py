class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [-inf] + [inf] * len(nums)
        for num in nums:
            dp[bisect_left(dp, num)] = num
        return bisect_left(dp, inf) - 1
