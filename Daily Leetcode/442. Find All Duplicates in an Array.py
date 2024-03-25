class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        lst = []

        for i in nums:
            x = abs(i)
            if nums[x - 1] < 0:
                lst.append(x)
            else:
                nums[x - 1] *= -1
        return lst