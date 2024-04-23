class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pset = []
        sset = []

        for i in pattern:
            if i not in pset:
                pset.append(i)
        for i in s.split(" "):
            if i not in sset:
                sset.append(i)
        
        temp_s = s.split(" ")

        if (len(pset) == len(sset)) and (len(pattern) != len(temp_s)):
            return False
        if len(pset) != len(sset):
            return False

        lst = []
        for i in range(len(pset)):
            temp = (pset[i], sset[i])
            lst.append(temp)
        # print(lst)

        for i in range(len(pattern)):
            x = (pattern[i], temp_s[i])
            # print(x)
            if x not in lst:
                return False
        # print(pset, sset)

        return True