class Solution:
    def largestOddNumber(self, num: str) -> str:
        all_odd = "13579"
        ans = ""

        for i in range(len(num) - 1,-1,-1):
            if num[i] in all_odd:
                ans =  num[:i+1:]
                break
        return ans

        
            