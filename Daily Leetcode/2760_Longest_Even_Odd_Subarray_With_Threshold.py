class Solution:
    def longestAlternatingSubarray(self, nums: List[int], t: int) -> int:
        ans = 0
        for i in range(len(nums)):
            count = 0
            if nums[i] % 2 == 0 and nums[i] <= t:
                count += 1
                while(i + 1 < len(nums)):
                    if nums[i] % 2 != nums[i + 1] % 2 and nums[i + 1] <= t:
                        count += 1
                    else:
                        break
                    i += 1
                ans = max(ans, count)

        return ans
        