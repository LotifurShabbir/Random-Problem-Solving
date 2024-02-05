class Solution:
    def firstUniqChar(self, s: str) -> int:
        ss = {}
        for i in s:
            if i in ss:
                ss[i] += 1
            else:
                ss[i] = 1
        for key, value in ss.items():
            if value == 1:
                return s.find(key)

        return -1