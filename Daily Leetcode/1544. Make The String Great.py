class Solution:
    def makeGood(self, s: str) -> str:
        lst = []
        for i in s:
            if lst and abs(ord(i) - ord(lst[-1])) == 32: # same capital and small char found
                lst.pop()
            else:
                lst.append(i)
        return ''.join(lst)
