class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i:i + len(needle)] == needle: #you can also use temp var for comparing
                return i
        return -1