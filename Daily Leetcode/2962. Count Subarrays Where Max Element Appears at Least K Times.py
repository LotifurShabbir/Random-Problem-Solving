class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res, max_n, max_cnt, l = 0, max(nums), 0, 0
        for r in range(len(nums)):
            if nums[r] == max_n:
                max_cnt += 1
            # one case (second case)
            while max_cnt > k or (max_cnt == k and nums[l] != max_n and l <= r):
                if nums[l] == max_n:
                    max_cnt -= 1
                l += 1
            if max_cnt == k:
                res += l + 1
        return res