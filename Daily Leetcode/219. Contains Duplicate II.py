class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictt = {}
        for i in range(len(nums)):
            if nums[i] not in dictt:
                dictt[nums[i]] = i
            elif nums[i] in dictt and abs(dictt[nums[i]] - i) <= k:
                return True
            dictt[nums[i]] = i # updating the new indices
        # print(dictt)
        return False