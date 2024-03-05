class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        n = len(s)
        j = n - 1
        while i < j:
            ch1 = s[i]
            ch2 = s[j]
            if ch1 != ch2:
                break
            else:
                while i <= j and ch1 == s[i]:
                    i += 1
                while i <= j and ch2 == s[j]:
                    j -= 1
        return j - i + 1

        