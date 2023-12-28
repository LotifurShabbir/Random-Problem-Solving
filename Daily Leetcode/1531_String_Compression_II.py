# Neetcode solution
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        cache = {}
        def func(i, k, prev, prev_count):
            if(i, k, prev, prev_count) in cache:
                return cache[(i, k, prev, prev_count)]
            if k<0:
                return float("inf")
            if i == len(s):
                return 0
            
            if s[i] == prev:
                incre = 1 if prev_count in [1,9,99] else 0
                ans = incre + func(i+1,k,prev,prev_count+1)
            else:
                ans = min(
                    func(i+1,k-1,prev,prev_count), #delete
                    1+func(i+1,k,s[i],1) #don't delete
                )
            
            cache[(i, k, prev, prev_count)] = ans

            return ans
        
        return func(0,k,"",0)