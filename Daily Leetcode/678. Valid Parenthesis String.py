class Solution:
    def checkValidString(self, s: str) -> bool:
        left, right, star = 0, 0, 0
        
        for char in s:
            if char == '(':
                left += 1
            elif char == ')':
                right += 1
            else:
                star += 1
                
            if right > left + star:
                return False
        
        left, right, star = 0, 0, 0
        
        for char in reversed(s):
            if char == '(':
                left += 1
            elif char == ')':
                right += 1
            else:
                star += 1
                
            if left > right + star:
                return False
        
        return True