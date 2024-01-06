class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] + 1

        total_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total_sum += nums[i]
            else:
                break

        nums.sort()
        arr = list(nums)
        for i in range(len(arr)):
            if total_sum not in arr:
                return total_sum
            else:
                total_sum += 1

        return arr[-1] + 1
