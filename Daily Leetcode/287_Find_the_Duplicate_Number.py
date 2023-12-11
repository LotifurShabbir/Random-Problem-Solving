class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = Counter(nums)
        for key, value in dic.items():
            if value > 1:
                return key