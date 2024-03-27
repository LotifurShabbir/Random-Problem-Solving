import numpy as np
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        lst = []
        for i in nums:
            if i > 0:
                lst.append(i)

        if not lst:
            return 1
        maxx = max(lst)
        arr = np.zeros(maxx, dtype  = int)
        for num in lst:
            arr[num - 1] = 1
        
        count = 0
        for i in range(len(arr)):
            if arr[i] != 1:
                return i + 1
                break
            else:
                count += 1

        if count == len(arr):
            return count + 1
        return len(lst) + 1