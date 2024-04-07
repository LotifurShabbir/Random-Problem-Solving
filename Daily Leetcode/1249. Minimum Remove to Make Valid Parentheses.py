class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:

        z = ""
        stack = []
        temp = set()

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if not stack:
                    temp.add(i)
                else:
                    stack.pop()

        while len(stack) != 0:
            temp.add(stack.pop())
        for i in range(len(s)):
            if i not in temp:
                z += s[i]
        return z
