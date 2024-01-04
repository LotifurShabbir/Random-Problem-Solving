class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        dic = Counter(nums)
        for key, value in dic.items():
            if value == 1:
                return -1
            ans += ceil(value / 3)
        return ans
        
        