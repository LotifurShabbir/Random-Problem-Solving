class Solution:
    def frequencySort(self, s: str) -> str:
        d = Counter(s)
        sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        result = ""
        
        for key, value in sorted_dict.items():
            result += str(key) * value
            
        return result