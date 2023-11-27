class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        sa = set(a)
        sb = set(b)

        if not sb.issubset(sa):
            return -1

        max_repeats = (len(b) // len(a)) + 2
        
        for i in range(1, max_repeats):
            if b in a * i:
                return i
                
        if b in a * max_repeats:
            return max_repeats

        return -1
