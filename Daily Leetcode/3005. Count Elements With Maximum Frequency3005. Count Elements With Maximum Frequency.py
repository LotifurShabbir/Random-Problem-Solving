class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ans = 0
        d = Counter(nums)
        maxx = max(d.values())
        
        for value in d.values():
            if value == maxx:
                ans += value
        return ans