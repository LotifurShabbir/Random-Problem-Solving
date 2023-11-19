class Solution:
    def maxFrequency(self, nums, k):
        nums.sort()
        left, right, ans = 0, 0, 0
        total = 0

        while right < len(nums):
            total += nums[right]

            while nums[right] * (right - left + 1) > total + k:
                total -= nums[left]
                left += 1

            ans = max(ans, right - left + 1)
            right += 1

        return ans
