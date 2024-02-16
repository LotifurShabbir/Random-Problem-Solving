class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        ans = -1
        total = 0

        for i in nums:
            if total > i:
                ans = total + i
            total += i

        return ans