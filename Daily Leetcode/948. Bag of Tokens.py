class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        ans = 0
        score = 0
        left, right = 0 , len(tokens) - 1
        while left <= right:
            if power >= tokens[left]:
                score += 1
                power -= tokens[left]
                left += 1
                ans = max(ans, score)
            elif score > 0 and power < tokens[left]:
                score -= 1
                power += tokens[right]
                right -= 1
                ans = max(score, ans)
            else:
                break

        return ans