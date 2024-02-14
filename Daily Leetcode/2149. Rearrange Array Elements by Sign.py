import numpy as np
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        plus = 0
        minus = 1
        plus_lst = []
        minus_lst = []

        for i in range(len(nums)):
            if nums[i] < 0:
                minus_lst.append(nums[i])
            elif nums[i] >= 0:
                plus_lst.append(nums[i])

        ans_lst_len = len(minus_lst) + len(plus_lst)
        ans_lst = np.zeros(ans_lst_len, dtype =  int)

        for i in range(len(plus_lst)):
            ans_lst[plus] = plus_lst[i]
            plus += 2
        
        for i in range(len(minus_lst)):
            ans_lst[minus] = minus_lst[i]
            minus += 2

        return ans_lst