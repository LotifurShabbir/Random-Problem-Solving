class Solution:
    def arrayStringsAreEqual(self, w: List[str], ww: List[str]) -> bool:
        check1 = ""
        check2 = ""
        for i in w:
            check1 += i
        for i in ww:
            check2 += i
        return check1 ==  check2
        