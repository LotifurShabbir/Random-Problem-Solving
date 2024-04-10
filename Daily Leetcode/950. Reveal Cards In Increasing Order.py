class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ans = [0] * len(deck)
        n = deque(range(0, len(deck)))
        print(n)
        for i in deck:
            idx = n.popleft()
            ans[idx] = i
            
            if n:
                n.append(n.popleft())

        return ans