class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        row, col = len(nums), len(nums[0])
        res = 0
        for i in range(col):
            lst = []
            for j in range(row):
                temp = max(nums[j])
                lst.append(temp)
                idx = nums[j].index(temp)
                nums[j][idx] = 0
            
            res += max(lst)

        return res