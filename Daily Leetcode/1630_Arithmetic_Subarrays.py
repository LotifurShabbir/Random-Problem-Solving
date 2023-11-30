class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(l)
        ans = []

        for i in range(n):
            diff = 0
            temp = nums[l[i]:r[i]+1]
            temp.sort()
            diff = temp[1] - temp[0]
            ans_bool = True

            for j in range(1,len(temp)):
                if(temp[j] - temp[j - 1] != diff):
                    ans_bool = False
                    break

            ans.append(ans_bool)

        return ans
        