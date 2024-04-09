class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count, i = 0, 0
        while True:
            # print(tickets)
            if i == len(tickets):
                i = 0
            if tickets[k] == 0:
                break
            if tickets[i] > 0:
                tickets[i] -= 1
                count += 1
            i += 1
        return count