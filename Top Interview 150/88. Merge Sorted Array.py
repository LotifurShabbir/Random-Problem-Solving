class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        itr = 0
        for i in range(m, len(nums1)):
            nums1[i] = nums2[itr]
            itr += 1
        print(nums1)
        
        # nums1.sort()
        
        for i in range(m + n - 1):
            mini = i
            for j in range(i + 1, len(nums1)):
                if nums1[j] < nums1[mini]:
                    mini = j
            nums1[i], nums1[mini] = nums1[mini], nums1[i]