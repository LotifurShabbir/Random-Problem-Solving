class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        ans = nums[0]
        nums.reverse()
        nums.pop()
        nums.sort()
        return ans + nums[0] + nums[1]

        