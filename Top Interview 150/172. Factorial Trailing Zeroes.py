# brute force recursive way
# this solution will give TLE for long N
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        def fact(x):
            if x == 1:
                return 1
            return x * fact(x - 1)
        temp = fact(n)
        count = 0
        temp = str(temp)
        for i in range(len(temp) - 1, -1, -1):
            if temp[i] == "0":
                count += 1
            else:
                break
        return count
# efficient way using math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while(n >= 5):
            n = n // 5
            count += n
        return count
# another math solution
class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = math.factorial(n)
        count = 0
        
        while num % 10 == 0: #means er last e ekta 0 acei
            count += 1
            num //= 10

        return count 