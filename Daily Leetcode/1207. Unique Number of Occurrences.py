class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = Counter(arr)
        lst = []
        for v in dic.values():
            if v in lst:
                return False
            lst.append(v)
        return True

        