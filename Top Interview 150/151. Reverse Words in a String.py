class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        lst = []
        ans = ""

        for i in range(len(s) - 1, -1, -1):
            if s[i] != "": #very strange about " " and ""
                lst.append(s[i])
        print(lst)

        for i in lst:
            ans = ans + i + " "

        ans = ans[:len(ans)- 1:]
        # print(ans)
        return ans
        
#shorter version and notes
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()[::-1]
        return ' '.join(words)
#notes for shorter version
'''
It uses `split()` to split the string into words, `[::-1]` to reverse the list of words, and `' '.join(words)` to concatenate the reversed words into a string with spaces in between.

'''      