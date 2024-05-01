class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        idx = word.index(ch)
        # print(idx)
        ans = ""
        for i in range(idx, -1, -1):
            ans += word[i]
        for i in range(idx + 1, len(word)):
            ans += word[i]
        return ans