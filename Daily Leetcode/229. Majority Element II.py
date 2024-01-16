class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # if len(nums) < 3:
        #     return nums
        # lst = []
        # nums.sort()
        # n = len(nums)
        # idx = n // 3
        # val = nums[idx]
        # for i in range(len(nums)):
        #     if nums[i] == val:
        #         lst.append(nums[i])

        # return set(lst)
        dic = Counter(nums)
        lst = []
        n = len(nums) // 3
        for key, value in dic.items():
            if value > n:
                lst.append(key)
        return lst