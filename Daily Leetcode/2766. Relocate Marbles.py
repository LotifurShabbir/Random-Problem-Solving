import numpy as np
class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        nums = set(nums)
        for i in range(len(moveFrom)):
            if moveFrom[i] in nums:
                nums.remove(moveFrom[i])
                nums.add(moveTo[i])
        
        a = list(nums)
        a.sort()
        
        return a
