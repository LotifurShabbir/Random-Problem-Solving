class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        ans = 0
        left = 0
        forbidden = set(forbidden)
        for i in range(len(word)):
            for j in range(i, max(left - 1, i - 10), -1):
                temp = word[j: i + 1]
                # print(temp)
                if temp in forbidden:
                    left = j + 1
                    break
            ans = max(ans, i - left + 1)

        return ans