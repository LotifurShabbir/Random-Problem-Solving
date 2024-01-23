class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        s = set(nums)
        #print(s)
        for i in range(n):
            temp = set()
            for j in range(i, n):
                temp.add(nums[j])
                if len(temp) == len(s):
                    ans += 1
        return ans