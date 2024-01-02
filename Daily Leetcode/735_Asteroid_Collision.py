class Solution:
    def asteroidCollision(self, astr: List[int]) -> List[int]:
        i = 0
        while i < len(astr) - 1:
            if astr[i] > 0 and astr[i + 1] < 0:
                if abs(astr[i]) == abs(astr[i + 1]):
                    astr.pop(i)
                    astr.pop(i)
                elif abs(astr[i]) > abs(astr[i + 1]):
                    astr.pop(i + 1)
                else:
                    astr.pop(i)
                i = max(0, i - 1)
            else:
                i += 1

        return astr
