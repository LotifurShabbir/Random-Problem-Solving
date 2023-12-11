class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic = Counter(arr)
        return max(dic, key = dic.get)
        # print(ans)
        # return ans
        