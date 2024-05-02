class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        for i in nums:
            if i * -1 in nums:
                return i * -1
        return -1