class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        n = len(arr)
        max_sum = [0] * n

        for i in range(n):
            max_val = float('-inf')

            for j in range(1, min(k, i + 1) + 1):
                max_val = max(max_val, arr[i - j + 1])

                prev_sum = max_sum[i - j] if i - j >= 0 else 0
                #print(prev_sum)
                max_sum[i] = max(max_sum[i], prev_sum + max_val * j)

        return max_sum[-1]
            