class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total_score = 0
        stack = []

        for i in operations:
            if i == "D":
                score = 2 * stack[-1] 
                total_score += score
                #print(score)
                stack.append(score)

            elif i == "C":
                rmv_scr = stack.pop()
                total_score -= rmv_scr

            elif i == "+":
                score = stack[-1] + stack[-2]
                total_score += score
                stack.append(score)

            else:
                score = int(i)
                total_score += score
                stack.append(score)

        return total_score
