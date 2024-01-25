class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = 0
        for i in range(len(digits)):
            temp = temp * 10 + digits[i]
        temp = str(temp + 1)
        temp = int(temp)
        print(temp)
        lst = []
        while(temp > 0):
            last_dig = temp % 10
            lst.append(last_dig)
            temp = temp // 10
        lst = lst[::-1]
        print(lst)
        return lst
#------Optimal Solution---------------
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits

        