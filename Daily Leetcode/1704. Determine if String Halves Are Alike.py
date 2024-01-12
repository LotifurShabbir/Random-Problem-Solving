class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        n = len(s)
        f, s , f_half, s_half = 0, 0, s[:n//2], s[n//2:]
        for i in f_half:
            if i in v:
                f += 1
        for i in s_half:
            if i in v:
                s += 1
        return f == s