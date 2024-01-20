class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        nums.sort()

        if len(nums) > 2 and nums[0] != nums[1]:
            return 1

        common_gcd = nums[0]
        
        for i in nums:
            common_gcd = gcd(common_gcd, i)
        #print(common_gcd)
        cnt = 1
        for i in nums:
            if i == common_gcd:
                cnt += 1

        return max(1, cnt // 2)