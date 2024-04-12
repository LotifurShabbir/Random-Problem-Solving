class Solution:
    def minOperationsToMakeMedianK(self, n: List[int], k: int) -> int:
        n.sort()
        ans = 0
        for i in range(0, len(n) // 2 + 1):
            ans += max(0, n[i] - k)

        for i in range(len(n) // 2, len(n)):
            ans += max(0, k - n[i])
            
        return ans