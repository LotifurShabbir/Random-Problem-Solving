class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        final = []
        dic = Counter(nums)
        while any(dic.values()):
            temp_list = []
            
            for key, value in dic.items():
                if value > 0:
                    temp_list.append(key)

            for key in temp_list:
                dic[key] -= 1

            final.append(temp_list)

        return final