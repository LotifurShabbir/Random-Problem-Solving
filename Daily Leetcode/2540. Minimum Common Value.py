#TLE Solution
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            for i in range(n1):
                if nums1[i] in nums2:
                    return nums1[i]
        elif n2 > n1:
            for i in range(n2):
                if nums2[i] in nums1:
                    return nums2[i]
        else:
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    return nums1[i]
        

        return -1