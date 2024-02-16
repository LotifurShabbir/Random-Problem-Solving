class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = Counter(arr)
        s = set(arr)
        
        sorted_dict = dict(sorted(d.items(), key = lambda item: item[1]))
        count = 0
        for key, value in sorted_dict.items():
            if value <= k and k != 0:
                count += 1
                k -= value
        
        return len(s) - count