class Solution:
    def canSortArray(self, nums: List[int]) -> bool:

        a = sorted(nums)
        for i in range(1, len(nums)):
            for j in range(1, len(nums)):
                if nums[j - 1] > nums[j] and bin(nums[j - 1]).count('1') == bin(nums[j]).count('1'): #overflowarcl
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
                    #print(nums[j-1])

        return a == nums

        